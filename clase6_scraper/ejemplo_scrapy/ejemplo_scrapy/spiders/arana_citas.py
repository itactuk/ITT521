import scrapy
from ..items import CitaItem


class AranaCita(scrapy.Spider):
    name = "citas"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        elemento = CitaItem()
        all_citas_div = response.css('.quote')

        for cita in all_citas_div:
            elemento['texto'] = cita.css(".text::text").extract()
            elemento['autor'] = cita.css(".author::text").extract()
            yield elemento

        link_siguiente = response.css(".next a::attr(href)").get()

        if link_siguiente is not None:
            yield response.follow(link_siguiente, callback=self.parse)
