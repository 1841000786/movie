# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 类似Django    orm中的models.py。
    # item不管什么字段都是scrapy.fields(),不区分intstr类型
    name= scrapy.Field()
