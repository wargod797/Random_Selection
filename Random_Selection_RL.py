# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 20:52:04 2019

@author: sridhar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the Dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Random Selection in Ads
import random
N=10000
d=10
ads_selected = []
total_reawrd =0
for i in range(0, N):
    ad = random.randrange(d)
    ads_selected.append(ad)
    reward = dataset.values[i,ad]
    total_reawrd = total_reawrd+reward
    
#Visulizing the Dataset
plt.figure(figsize=(26.6666,15))
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()