#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 22:45:17 2019

@author: danielgeneau
"""
#Packages 
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


#Generate random normally distributed data with a mean of 1.75, SD of 0.8 and 5000 samples

                                #(mean, SD, number of samples) ?)

r_data= np.round(np.random.normal(0, 12, 5000),2)
plt.scatter(r_data, r_data)


#calculate the mean, median and Mode of the data set 

m1= np.mean(r_data)
m2= np.median(r_data)
m3= stats.mode(r_data)

#plot data as a histogram with 10 bins 

plt.hist(r_data)


plt.show()

#plot data as a histogram with 20 black bins 

plt.hist(r_data, bins=20, color= "black")

plt.show()


#plot data as a histogram with 100 green bins
plt.hist(r_data, bins=100, color="green")

plt.show()



#calculate variance of data

variance= np.var(r_data)
print(variance)












