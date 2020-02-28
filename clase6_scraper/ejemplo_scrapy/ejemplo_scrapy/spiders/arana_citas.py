import scrapy


class AranaCita(scrapy.Spider):
    name = "citas"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    def parse(self, response):
        pass
