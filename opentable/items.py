# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OpentableItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rest_name = scrapy.Field()
    rating_list = scrapy.Field()
    num_reviews_list = scrapy.Field()
    expensive = scrapy.Field()
    genre = scrapy.Field()
    location = scrapy.Field()
    booked_today_list = scrapy.Field()
    delivery = scrapy.Field()
    #delivery_partners = scrapy.Field()

