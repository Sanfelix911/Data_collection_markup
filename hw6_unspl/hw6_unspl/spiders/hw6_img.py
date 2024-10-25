import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from ..items import Hw6UnsplItem
from itemloaders.processors import MapCompose
import json


class Hw6ImgSpider(CrawlSpider):
    name = "hw6_img"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/t/food-drink"]

    rules = (Rule(LinkExtractor(restrict_xpaths="//div[@class='JM3zT']"), callback="parse_item", follow=True),)

    def parse_item(self, response):
        loader = ItemLoader(item=Hw6UnsplItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)

        loader.add_xpath("author_name", "//a[@class = 'vGXaw uoMSP kXLw7 R6ToQ JVs7s R6ToQ']/text()")

        categories = response.xpath("//a[@class = 'm7tXD jhw7y TYpvC']/text()").getall()
        loader.add_value('categories', categories)

        description = response.xpath("//h1[@class = 'vev3s']/text()").get()
        loader.add_value('description', description)

        image_url = response.xpath("//div[@class='WxXog']/@src").get()
        loader.add_value('image_urls', image_url)

        yield loader.load_item()

