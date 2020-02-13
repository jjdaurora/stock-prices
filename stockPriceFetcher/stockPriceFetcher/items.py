# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockpricefetcherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    date = scrapy.Field()
    openPrice = scrapy.Field()
    highPrice = scrapy.Field()
    lowPrice = scrapy.Field()
    closePrice = scrapy.Field()
    volume = scrapy.Field()    
    
    pass
