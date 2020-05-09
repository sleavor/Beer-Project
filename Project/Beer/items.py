# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field  

class BeerItem(scrapy.Item):
    # define the fields for your item here like:
    beerName = scrapy.Field()
    brewery = scrapy.Field()
    beerPrice = scrapy.Field()
    beerSize = scrapy.Field()
    beerABV = scrapy.Field()
    beerRegion = scrapy.Field()
    beerCountry = scrapy.Field()
    beerPricePerOz = scrapy.Field()
    beerBARating = scrapy.Field()
    beerNumBARatings = scrapy.Field()

class BAItem(scrapy.Item): 
   name = scrapy.Field() 
   rating = scrapy.Field()
   abv = scrapy.Field()
   style = scrapy.Field()
   numRatings = scrapy.Field() 
   brewery = scrapy.Field()
