# -*- coding: utf-8 -*-
import scrapy
from Beer.items import BeerItem
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import TakeFirst

class MinibarSpider(CrawlSpider):
    name = 'minibar'
    allowed_domains = ['https://minibardelivery.com']
    start_urls = [
        'https://minibardelivery.com/store/category/beer',
        ]
    
    rules = (
        Rule(LinkExtractor(allow=('/product/')), callback='parse_beer'),

    )

    def parse_beer(self, response):
        l = ItemLoader(item=BeerItem(), response=response)
        l.add_xpath('beerName', '//h1/a/text()', TakeFirst())
        l.add_xpath('brewery', '//h2/a/text()', TakeFirst())
        l.add_xpath('beerPrice', '//span[@class="c1nf6r c37jbv jkw37r"]/text()')
        l.add_xpath('beerABV', '//td[@class="aoyeow c35d1a eb68uj edh3tw jkywcj"]/text()', TakeFirst())
        l.add_xpath('beerRegion', '//td[@class="aoyeow c35d1a eb68uj edh3tw jkywcj"]/text()')
        l.add_xpath('beerCountry', '//td[@class="aoyeow c35d1a eb68uj edh3tw jkywcj/text()')
        l.add_xpath('beerSize', '//span[@class="c1nf6r c39pmg"]/text()')
        return l.load_item()


