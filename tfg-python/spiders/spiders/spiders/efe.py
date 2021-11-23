from urllib.request import urlopen

import scrapy
from datetime import datetime
from bs4 import BeautifulSoup


class EFEBulos(scrapy.Spider):
    name = 'efeSpider'

    start_urls = [
        'https://verifica.efe.com/verificaciones/'
    ]

    def parse(self, response):
        for titularbulo in response.xpath("//h3[@class='post_title entry-title']"):
            detalletitular = titularbulo.xpath('./a/@href').get()
            yield scrapy.Request(
                url=response.urljoin(detalletitular),
                callback=self.parse_detalle_titular,
                cb_kwargs={
                    'link_titular': response.urljoin(detalletitular)
                }
            )

        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        print("Siguiente pagina")
        print(next_page)
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_detalle_titular(self, response, link_titular):
        fecha = response.xpath("//span[contains(@class, 'post_meta_item post_date')]/text()").get().strip()
        fecha_formateada = datetime.strptime(fecha, "%d de %B de %Y")
        origen=response.xpath("//p/img/@src").get()

        yield {
            'titular': response.xpath("//h1[@class='sc_layouts_title_caption']/text()").get().strip(),
            'link_titular': link_titular,
            'fecha': fecha_formateada,
            'origen': origen
        }
