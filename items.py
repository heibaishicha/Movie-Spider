# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 主题
    title = scrapy.Field()
    # 评分
    rate = scrapy.Field()
    # ID
    id = scrapy.Field()
    pass

