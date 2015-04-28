from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from jobs.items import JobsItem

class HasJobSpider(CrawlSpider):
	
	name='hasjob'
	allowed_domains = ['hasjob.co']
	start_urls = ['https://hasjob.co']
	rules = [Rule(LinkExtractor(restrict_xpaths='//*[@id="stickie-area"]/li', tags='a'), 'parse_jobs')]
	
	def parse_jobs(self, response):
		torrent = JobsItem()
		torrent['title'] = response.css('h1[itemprop="name"]::text').extract();
		torrent['location'] = response.css('#post-location span[itemprop="name"]::text').extract();
		torrent['post_url'] = response.url
		torrent['organization'] = response.css('strong[itemprop="name"]::text').extract();	
		torrent['organization_url']  = response.css('#post-location + a::text').extract();
		torrent['job_type'] = response.css('a[href^="/type"]::text').extract();
		torrent['job_category'] = response.css('a[href^="/category"]::text').extract();
		torrent['salary'] = ''
		
		
		yield torrent
