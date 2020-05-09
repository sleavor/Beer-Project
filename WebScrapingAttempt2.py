# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 19:07:49 2020

@author: Shawn Leavor
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get("https://www.totalwine.com/beer/c/c0010?viewall=true&page=1&pageSize=120")

products=[] #List to store name of the product
prices=[] #List to store price of the product
pack_sizes=[] #List size of bottle
pricePeroz=[] #Cost of each ounce of beer
TWratings=[] #Ratings for beer
BAratings=[] #Ratings for beer from BA

for page in range(18):
    articles = []
    for i in range(1,120,1):
        beer_xpath = '/html/body/div/div/div/main/div/div[2]/div[2]/div/article[' + str(i) + ']/div[2]/h2/a'
        beer_link = driver.find_element_by_xpath(beer_xpath)
        articles.append(beer_link)
    x = 0
    for article in articles:
        try:
            article.click()
        except StaleElementReferenceException as Exception:
            print('StaleElementReferenceException while trying to click next link')
            beer_xpath = '/html/body/div/div/div/main/div/div[2]/div[2]/div/article[' + str(x) + ']/div[2]/h2/a'
            beer_link = driver.find_element_by_xpath(beer_xpath)
            beer_link.click()
        for j in range(1,3):
            try:
                container_xpath = '/html/body/div/div/div/main/div/div/div[4]/div/div/div[3]/div/div[5]/div/div[' + str(j) + ']'
                container = driver.find_element_by_xpath(container_xpath)
                if container.text == 'Can' or container.text() == 'Bottle':
                    container.click()
                    size_xpath = '/html/body/div/div/div/main/div/div/div[4]/div/div[3]/div/div[5]/div[2]/fieldset[2]/div/div/ul'
                    sizer = driver.find_element_by_xpath(size_xpath)
                    for child in sizer.find_elements_by_xpath(".//*"):
                        if "Single" in child.text:
                            child.click()
                            beerName = driver.find_element_by_class_name('productTitle__3XDd9UVh')
                            products.append(beerName.text)
                            beerSize = driver.find_element_by_class_name('productSubTitle__3sTXP-XD')
                            pack_sizes.append(beerSize.text)
                            beerPrice = driver.find_element_by_id('edlpPrice')
                            Size = beerSize.text
                            prices.append(beerPrice.text)
                            Price=beerPrice.text
                            if "oz" in Size:
                                ozs = Size[0:2]
                                price = Price[-1:0]
                                pricePeroz.append(ozs/price)
                            elif "ml" in Size:
                                ozs = Size[0:3]*0.03519503
                                price = Price[-1:0]
                                pricePeroz.append(ozs/price)
                            beerTWRating = driver.find_element_by_class_name('bv_avgRating')
                            driver.back()
            except:
                pass
        driver.back()
        x += 1
    next_page = article.find_element_by_class_name("NextArrow")
    next_page.click()

for beer in products:
    BASearchUrl = 'https://www.beeradvocate.com/search/?q=' + urllib.parse.quote_plus(beer.text)
    driver.get(BASearchUrl)
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    BAUrl = soup.find('a', href=True, attrs={'class':'gs-title'})
    driver.get(BAUrl['data-ctorig'])
    content = driver.page_source
    soup = BeautifulSoup(content)
    
    BArating = soup.find('span', attrs={'class':'ba-ravg'})
    BAratings.append(BArating.text)