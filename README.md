The following repository is my repository for a beer data scraping project

The Project folder contains a Scrapy project which was used to scrape the data from beeradvocate.com. The specific spider is in spiders/beeradvocate.py. It cycles through each URL for beer and grabs the beer name, brewery, beer style, abv, rating, and number of ratings.

AveragesPerStyleAndBrewery runs through the data to grab the average rating for each style of beer and each brewery and finds the max and min average style and brewery.

BeerGraphsByStyle creates a graph of ABV and rating for each beer of a particular style

BeerGraphsForAllData creates a graph that plots all the data on one graph (be warned that it's hard to decipher anything)

MissingData plots a graph using missingno to find what data is missing

WebScraping and WebScrapingAttempt2 were two failures at trying to grab the data using beautiful soup and selenium