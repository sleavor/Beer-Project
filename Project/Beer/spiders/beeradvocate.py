# -*- coding: utf-8 -*-
import scrapy
from Beer.items import BAItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class BeeradvocateSpider(scrapy.Spider):
    name = 'beeradvocate'
    allowed_domains = ['beeradvocate.com']
    start_urls = []
    for i in range (280570,481341):
        start_urls.append('https://beeradvocate.com/beer/profile/50/' + str(i))
    #start_urls = [urls]


    def parse(self, response):
        abvAndScore = response.xpath('//div[@id="info_box"]/div/dl/dd/span/b/text()').extract()
        item = BAItem()
        item['name'] = response.xpath('//h1/text()').extract()
        item['rating'] = response.xpath('//span[@class="ba-ravg Tooltip"]/text()').extract()
        if abvAndScore != []:
            item['abv'] = abvAndScore[0]
        item['style'] = response.xpath('//div[@id="info_box"]/div/dl/dd/a/b/text()').extract()
        item['numRatings'] = response.xpath('//span[@class="ba-ratings Tooltip"]/text()').extract()
        item['brewery'] = response.xpath('//h1/span/text()').extract()
        yield item
