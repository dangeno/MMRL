#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:55:56 2019

@author: danielgeneau
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


#import data and label columns
data= pd.read_table("http://www.krigolsonteaching.com/uploads/4/3/8/4/43848243/sampleanovadata.txt", 
                    header = None)
data.columns=['Subject', 'Group', 'rt']


#split by group
G1=data[data['Group']==1]['rt']
G2=data[data['Group']==2]['rt']
G3=data[data['Group']==3]['rt']

#Check anova assumptions! 

#Check for normality 

H1= plt.hist(G1, 
             bins=30)
plt.show()
H2= plt.hist(G2, 
             bins=30)
plt.show()
H3= plt.hist(G3, 
             bins=30)
plt.show()


#Skewness and Kertosis

k1= stats.kurtosis(G1)
s1= stats.skew(G1)


k2= stats.kurtosis(G2)
s2= stats.skew(G2)


k3= stats.kurtosis(G3)
s3= stats.skew(G3)


#QQ plots for normaility 

stats.probplot(G1, plot= plt)
plt.title('Group 1 QQ Plot')
plt.show()

stats.probplot(G2, plot= plt)
plt.title('Group 2 QQ Plot')
plt.show()

stats.probplot(G3, plot= plt)
plt.title('Group 3 QQ Plot')
plt.show()


#Sharpiro test for normaility 


sh1= stats.shapiro(G1)

sh2= stats.shapiro(G2)

sh3= stats.shapiro(G3)



#Homogeneity of Variance 

v1= np.var(G1)

v2= np.var(G2)

v3= np.var(G3)


#Bartlett test  I cant figure out the length thingy!!!

b1= stats.bartlett(data['rt'], data['Group'])


l1= stats.levene(data['rt'], data['Group'])


#Box plots

plt.boxplot([G1,G2,G3])
plt.title('Group Comparison Box Plots')
plt.xlabel('Group Number')
plt.ylabel('Score')
plt.show()






#Anova 

Anova= stats.f_oneway(G1, G2, G3)






