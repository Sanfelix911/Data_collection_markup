# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Hw6UnsplItem(scrapy.Item):
    author_name = scrapy.Field()
    description = scrapy.Field()
    categories = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
