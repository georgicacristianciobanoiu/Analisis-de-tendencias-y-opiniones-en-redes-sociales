import scrapy
import re
from datetime import datetime


class FactualBulos(scrapy.Spider):
    name = 'factualSpider'

    start_urls = [
        'https://factual.afp.com/list'
    ]

    def parse(self, response):
        for titularbulo in response.xpath("//main//div[@class='card']"):
            detalletitular = titularbulo.xpath("./a/@href").get()
            yield scrapy.Request(
                url=response.urljoin(detalletitular),
                callback=self.parse_detalle_titular,
                cb_kwargs={
                    'link_titular': response.urljoin(detalletitular)
                }
            )

        next_page = response.xpath(
            "//ul[@class='pagination pagination-sm justify-content-end m-0']/li/a/@href").get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_detalle_titular(self, response,link_titular):
        titular = response.xpath("//h1[@class='content-title']/text()").get()
        fecha = response.xpath("//span[@class='meta-date']/span[@class='day hide']/@timestamp").get()
        fecha_formateada = datetime.fromtimestamp(int(fecha))
        contenido_titular = response.xpath("//div[@class='article-entry clearfix']").get()

        # Expresion regular para detectar los links de tipo https://perma.cc que es donde estan las capturas de tuits
        # o publicaciones en facebook comentando el bulo
        # FUNCIONA BIEN origen_noticia = re.findall('(http:\/\/|https:\/\/)([perma]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])?',contenido_titular)
        origen_noticia = re.findall('(https:\/\/perma\.cc\/)([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])',contenido_titular)
        links_origen = []
        for elem in origen_noticia:
            link = ''.join(elem)
            links_origen.append(link)

        yield {
            'titular': titular.strip(),
            'link_titular': link_titular,
            'fecha': fecha_formateada,
            'origen': links_origen
        }
