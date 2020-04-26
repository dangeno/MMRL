#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:44:19 2019

@author: danielgeneau
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


my_data= pd.read_table('https://www.krigolsonteaching.com/uploads/4/3/8/4/43848243/assignmentdata2.txt', 
                       header = None)
my_data.columns=['Subject', 'Group', 'score']


G1=my_data[my_data['Group']==1]['score']
G2=my_data[my_data['Group']==2]['score']


#Checking for outliers Box Plots 

plt.boxplot([G1,G2])
plt.title('Group 1 vs. Group 2 Scores')
plt.xlabel('Group Number')
plt.ylabel('Score')
plt.show()

G1mean=np.mean(G1)
G2mean=np.mean(G2)

G1std= np.std(G1)
G2std= np.std(G2)

labels = ['1', '2']
x_pos = np.arange(len(labels))
Means = [G1mean, G2mean]
error = [G1std, G2std]

fig, ax = plt.subplots()
ax.bar(x_pos, Means,
       yerr=error,
       align='center',
       alpha=0.25,
       ecolor='black',
       capsize=10)
ax.set_ylabel('Means')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Comparison of Group Means with Error')
ax.yaxis.grid(True, 
              alpha=0.4)

plt.show()

#difference score

#??

#QQ plots 
stats.probplot(G1, plot= plt)
plt.title('Group 1 QQ Plot')
plt.show()

stats.probplot(G2, plot= plt)
plt.title('Group 2 QQ Plot')
plt.show()

#pairwise ttest
test= stats.ttest_rel(G1,G2)






