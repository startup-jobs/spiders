# -*- coding: utf-8 -*-
import scrapy


class SpringroleSpider(scrapy.Spider):
    name = "springrole"
    allowed_domains = ["springrole.com"]
    start_urls = (
        'http://www.springrole.com/',
    )

    def parse(self, response):
        pass
