import scrapy


class NewtralBulos(scrapy.Spider):
    name = 'newtralSpider'

    start_urls = [
        'https://www.newtral.es/zona-verificacion/fakes/'
    ]

    def parse(self, response):
        for titularbulo in response.xpath("//section[@class='s-verification-cards']//div[@class='o-section c-card__verification__container']/article//div[@class='c-card__verification__quote-container']/mark"):
            print("Hola")
            print(titularbulo)
            detalletitular = titularbulo.xpath("./a/@href").get()
            print(detalletitular)
            yield scrapy.Request(
                url=response.urljoin(detalletitular),
                callback=self.parse_detalle_titular
            )

    def parse_detalle_titular(self, response):
        titular = response.xpath("//h1[@class='entry-title c-article__title']/text()").get()
        fecha = response.xpath("//time/@datetime").get()
        yield {
            'titular_newtral': titular.strip(),
            'fecha': fecha,
        }
