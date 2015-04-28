# -*- coding: utf-8 -*-
import scrapy


class SpringroleSpider(scrapy.Spider):
    name = "springrole"
    allowed_domains = ["springrole.com", "3b4vpnaaj6-dsn.algolia.net"]
    start_urls = (
	'https://3b4vpnaaj6-dsn.algolia.net/1/indexes/*?X-Algolia-Application-Id=3B4VPNAAJ6&X-Algolia-API-Key=d284fa96d3869b371d1f3d1166faaa97&0=%2F1%2Findexes%2Fjobs%3Fquery%3D%26hitsPerPage%3D10%26page%3D0%26facets%3Dcountry%252Ccity%26facetFilters%3D%255B%2522country%253AIndia%2522%255D%26numericFilters%3D%255B%2522published%253D1%2522%255D&'
    )

    def parse(self, response):
	data = json.loads(response.body_as_unicode())
#	for job in data.results[0].hits
#		puts job['url']
	#	puts job['title']
        pass
