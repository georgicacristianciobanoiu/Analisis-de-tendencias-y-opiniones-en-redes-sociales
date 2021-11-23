from urllib.request import urlopen

import scrapy
from datetime import datetime
from bs4 import BeautifulSoup


class EFEBulos(scrapy.Spider):
    name = 'oldefeSpider'

    start_urls = [
        'https://www.efe.com/efe/espana/efeverifica/50001435'
    ]

    def parse(self, response):
        for titularbulo in response.xpath("//div[@class='efe-listacatact  efe-lista2col']/ul/li/article"):
            detalletitular = titularbulo.xpath('./a/@href').get()
            yield scrapy.Request(
                url=response.urljoin(detalletitular),
                callback=self.parse_detalle_titular,
                cb_kwargs={
                    'link_titular': response.urljoin(detalletitular)
                }
            )

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_link, callback=self.parse)

    def parse_detalle_titular(self, response, link_titular):
        fecha = response.xpath("//span[@class='fecha']/time/@datetime").get()
        fecha_formateada = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%SZ")
        '''soup = BeautifulSoup(urlopen(response.url), "lxml")
        iframes = soup.find_all('iframe')

        for origin_link in iframes:
            print("hola")
            print(origin_link)
            # origen.append(twitter_link.xpath("./iframe/@src").get())'''
        yield {
            'titular': response.xpath("//div[@class='head']/h1/text()").get().strip(),
            'link_titular': link_titular,
            'fecha': fecha_formateada,
        }
