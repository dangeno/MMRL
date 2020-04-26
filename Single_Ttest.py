#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:06:17 2019

@author: danielgeneau
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd


my_data= pd.read_table('https://www.krigolsonteaching.com/uploads/4/3/8/4/43848243/assignmentdata1.txt', 
                       header = None)
my_data.columns=['score']

#mean
mean=np.mean(my_data)

#boxplot
plt.boxplot(my_data['score'])
plt.title('Box Plot')
plt.xlabel('Group Number')
plt.ylabel('Score')
plt.show()



#Bar plots with error bars


std= np.std(my_data['score'])


labels = ['1']
x_pos = np.arange(len(labels))

error = std

fig, ax = plt.subplots()
ax.bar(x_pos, mean,
       yerr=error,
       align='center',
       alpha=0.5,
       ecolor='black',
       capsize=10)
ax.set_ylabel('Mean')
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.set_title('Comparison of Group Means with Error')
ax.yaxis.grid(True, 
              alpha=0.4)

plt.show()




#single sample T-test

test= stats.ttest_1samp(my_data,0)



