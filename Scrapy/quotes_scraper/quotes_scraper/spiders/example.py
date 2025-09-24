import scrapy


class ExampleSpider(scrapy.Spider):
    name = "example"
    allowed_domains = ["google.com"]
    start_urls = ["https://google.com"]

    def parse(self, response):
        pass
