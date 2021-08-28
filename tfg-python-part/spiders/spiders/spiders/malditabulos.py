import scrapy
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'esp_esp')


class MalditaBulosSpdier(scrapy.Spider):
    name = 'malditaBulosSpider'

    start_urls = [
        'https://maldita.es/malditobulo/1'
    ]

    def parse(self, response):
        for titularbulo in response.xpath("//div[@class='section-card flex flex-col md:flex-row']"):
            titular = titularbulo.xpath(".//div[@class='section-card-headline']/a/text()").get()
            detalletitular = titularbulo.xpath(".//div[@class='section-card-headline']/a/@href").get()
            yield scrapy.Request(
                url=response.urljoin(detalletitular),
                callback=self.parse_detalle_titular,
                cb_kwargs={
                    'titular': titular,
                    'link_titular': response.urljoin(detalletitular)
                }
            )

        next_page = response.xpath(
            "//span[@class='bg-white text-gray-800 px-3 py-2 text-lg border-r border-gray-400']/a/@href").get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_detalle_titular(self, response, titular, link_titular):
        fecha = response.xpath("//div[@id='article-date']/span[@class='meta-value']/text()").get()
        origen = response.xpath("//img[@id='article-featured-image']/@src").get()
        fecha = fecha.split(sep=",", maxsplit=2)
        fecha_formateada = datetime.strptime(fecha[1].strip(), "%d %B %Y")
        yield {
            'titular': titular,
            'link_titular': link_titular,
            'fecha': fecha_formateada,
            'origen': origen,
        }
