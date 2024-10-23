import scrapy
from scrapy.http import HtmlResponse
from gb_analist.items import GbAnalistItem


class GbCataligSpider(scrapy.Spider):
    name = "gb_catalig"
    allowed_domains = ["gb.ru"]
    start_urls = ["https://gb.ru/courses/analytics"]

    def parse(self, response : HtmlResponse):
        links = response.xpath("//a[@class = 'card_full_link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.analist)
       

    def analist (self, response : HtmlResponse):
        name = response.xpath("//span[@class = '_text-cover']/text()")
        title = response.xpath("//div/div[@class = 'profession-info-card _theme-white ui-col-sm-6']/text()")
        url = response.url
        yield GbAnalistItem(name = name, title = title, url = url)