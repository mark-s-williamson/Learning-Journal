import scrapy


class Example2Spider(scrapy.Spider):
    name = "example2"
    allowed_domains = ["example.com"]
    start_urls = ["https://example.com"]

    def parse(self, response):
        pass
