# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:12:19 2020

@author: Shawn Leavor
"""

import pandas as pd
import missingno as msno 

df = pd.read_csv('Project\Beer\data.csv', na_values=['','0'])

msno.matrix(df) 
