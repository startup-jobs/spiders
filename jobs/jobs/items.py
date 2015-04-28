# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    post_url = scrapy.Field()
    organization = scrapy.Field()
    organization_url = scrapy.Field()
    job_type = scrapy.Field()
    job_category = scrapy.Field()
    salary = scrapy.Field()			
