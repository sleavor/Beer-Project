# -*- coding: utf-8 -*-
"""
Created on Sat May  9 17:40:25 2020

@author: Shawn Leavor
"""
import pandas as pd
import numpy as np

df = pd.read_csv('Project\Beer\data.csv', na_values=['','0'])
df = df.dropna(how='any',axis=0)
df = df[df.abv.str.contains("%")]

for num in range(1,25):
    num = str(num)
    df = df[df.numRatings != num]

allStyles=[]
allBreweries = []

#Averages Per Beer Style
for style in df['style']:
    if style not in allStyles:
        allStyles.append(style)

styleRatings = {}

for style in allStyles:
    newdf = df[df['style'].str.contains(style)]
    aCount = 0 
    sumRate = 0
    for rating in newdf['rating']:
        aCount += 1
        sumRate += rating
    if aCount != 0:
        styleRatings[style] = sumRate/aCount

miniStyle = 5
maxiStyle = 0
for style in styleRatings:
    if styleRatings[style] > maxiStyle:
        maxStyle = style
        maxiStyle = styleRatings[style]
    if styleRatings[style] < miniStyle:
        minStyle = style
        miniStyle = styleRatings[style]
    
#Averages Per Brewery
for brewery in df['brewery']:
    if brewery not in allBreweries:
        allBreweries.append(style)

breweryRatings = {}

for brewery in allBreweries:
    newdf = df[df['brewery'].str.contains(style)]
    aCount = 0 
    sumRate = 0
    for rating in newdf['rating']:
        aCount += 1
        sumRate += rating
    if aCount != 0:
        breweryRatings[brewery] = sumRate/aCount

miniBrewery = 5
maxiBrewery = 0
for brewery in breweryRatings:
    if breweryRatings[brewery] > maxiBrewery:
        maxBrewery = brewery
        maxiBrewery = breweryRatings[brewery]
    if breweryRatings[brewery] < miniBrewery:
        minBrewery = brewery
        miniBrewery = breweryRatings[brewery]