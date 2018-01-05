# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PropertyItem(scrapy.Item):
    title = scrapy.Field()
    posted_at = scrapy.Field()
    created_at = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    owner = scrapy.Field()
    phone = scrapy.Field()
    image = scrapy.Field()
    description = scrapy.Field()
    property_type = scrapy.Field()
    tax = scrapy.Field()
    area = scrapy.Field()
    rooms = scrapy.Field(serializer=int)
    garage = scrapy.Field(serializer=int)
    city = scrapy.Field()
    cep = scrapy.Field()
    district = scrapy.Field()
    source = scrapy.Field()
