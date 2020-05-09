# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 19:15:43 2020

@author: Shawn Leavor
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import urllib
import random

driver = webdriver.Chrome()

urls = [] # List of urls to scrape
beerurls = [] # List of all beer products

driver.get("https://www.totalwine.com/sitemap.xml")
content = driver.page_source
soup = BeautifulSoup(content)

for url in soup.find_all('loc'):
    a = url.text
    if a[27:34] == "Product":
        urls.append(a)

for url in urls:
    time.sleep(random.randint(5,10))
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for item in soup.find_all('loc'):
        a = item.text
        if a[26:30] == "beer":
            beerurls.append(a)

products=[] #List to store name of the product
prices=[] #List to store price of the product
pack_sizes=[] #List size of bottle
pricePeroz=[] #Cost of each ounce of beer
TWratings=[] #Ratings for beer
BAratings=[] #Ratings for beer from BA

for url in beerurls:
    time.sleep(random.randint(10,20))
    
    try:
        driver.get(url+'-1')
    except:
        continue
    
    # content = driver.page_source
    # soup = BeautifulSoup(content)
    # product = soup.find('h1', attrs={'class':'productTitle__3XDd9UVh'})
    # price = soup.find('div', attrs={'id':'edlpPrice'})
    # package = soup.find('h2', attrs={'class':'productSubTitle__3sTXP-XD'})
    # rating = soup.find('button', attrs={'id':'avg-rating-button'})
    product = driver.find_element_by_class_name("productTitle__3XDd9UVh")
    price = driver.find_element_by_id('edlpPrice')
    package = driver.find_element_by_class_name('productSubTitle__3sTXP-XD')
    try:
        rating = driver.find_element_by_id('avg-rating-button')
    except:
        rating = "N/A"
    
    if product != None and price != None:
        packageTxt = package.text
        pricetxt=price.text
        if len(packageTxt) <= 5:
            try:
                pack_size = int(packageTxt[0:-3])
                unit = packageTxt[-2:]
            except:
                continue
        else:
            try:
                pack_size = int(packageTxt[0:-6])
                unit = packageTxt[-6:-4]
            except:
                continue

        try:
            if unit == 'oz' or unit == 'OZ':
                ozPrice = float(pricetxt[1:])/pack_size
            elif unit == 'ml' or unit == 'ML':
                ozPrice = float(pricetxt[1:])/(pack_size*0.033814)
        except:
            continue
            
        products.append(product.text)
        prices.append(price.text)
        pack_sizes.append(pack_size)
        pricePeroz.append(ozPrice)
        
        if rating != None:
            TWratings.append(rating.text)
        else:
            TWratings.append(None)
            
        BASearchUrl = 'https://www.beeradvocate.com/search/?q=' + urllib.parse.quote_plus(product.text)
        driver.get(BASearchUrl)
        content = driver.page_source
        soup = BeautifulSoup(content)
        
        BAUrl = soup.find('a', href=True, attrs={'class':'gs-title'})
        driver.get(BAUrl['data-ctorig'])
        content = driver.page_source
        soup = BeautifulSoup(content)
        
        BArating = soup.find('span', attrs={'class':'ba-ravg'})
        BAratings.append(BArating.text)
        
    
df = pd.DataFrame({'Product Name':products,'Price':prices, 'Size':pack_sizes, 'Price per Oz':pricePeroz, 'TW Rating':TWratings, 'BA Ratings':BAratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')


