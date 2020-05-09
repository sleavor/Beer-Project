# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 22:48:26 2020

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
        
#Plot All Beers
plt.scatter(x,y, s=1)
plt.xlim([0, 25])
plt.show()

#Sort all beers by style and plot
for style in allStyles:
    newdf = df[df['style'].str.contains(style)]
    x=[]
    y = newdf['rating']
    for abv in newdf['abv']:
        if "%" in abv:
            a=abv.split('%'[0])
            x.append(float(a[0]))
    plt.scatter(x,y, label=style, s=1)

plt.title("Beer Ratings by ABV and Style")
plt.xlim([0,25])
plt.xlabel('abv')
plt.ylim([1,5])
plt.ylabel('average rating')
plt.xlim([0,25])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()