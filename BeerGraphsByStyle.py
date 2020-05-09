# -*- coding: utf-8 -*-
"""
Created on Sat May  2 13:01:02 2020

@author: Shawn Leavor
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Project\Beer\data.csv', na_values=['','0'])
df = df.dropna(how='any',axis=0)
df = df[df.abv.str.contains("%")]

for num in range(1,25):
    num = str(num)
    df = df[df.numRatings != num]

allStyles = []
x = []
y = df['rating']

for abv in df['abv']:
    if "%" in abv:
        a = abv.split('%'[0])
        x.append(float(a[0]))

for style in df['style']:
    if style not in allStyles:
        allStyles.append(style)
        
# Plot beer graph for each style
for style in allStyles:
    newdf = df[df['style'].str.contains(style)]
    x=[]
    y = newdf['rating']
    count = 0
    sumRating = 0
    for abv in newdf['abv']:
        if "%" in abv:
            a=abv.split('%'[0])
            x.append(float(a[0]))
    plt.scatter(x,y, label=style, s=1.5)
    plt.title(style)
    plt.xlim([0,25])
    plt.xlabel('abv')
    plt.ylim([1,5])
    plt.ylabel('average rating')
    plt.show()
