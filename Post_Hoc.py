#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:03:38 2019

@author: danielgeneau
"""
import scikit_posthocs as sp
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import statsmodels.api as sm




data= pd.read_table("https://www.krigolsonteaching.com/uploads/4/3/8/4/43848243/sampleanovadata2.txt", 
                    header = None)
data.columns=['Subject', 'Group', 'rt']

#Groupings 
G1=data[data['Group']==1]['rt']
G2=data[data['Group']==2]['rt']
G3=data[data['Group']==3]['rt']
G4=data[data['Group']==4]['rt']

#anova


A1= stats.f_oneway(G1,G2,G3,G4)


#Post-Hoc analysis


tt= sp.posthoc_ttest(A1)
Tuk= sp.posthoc_tukey_hsd('rt','Group', alpha=0.04)
 

#Princple component anlysis 
#Support Vector Machine learning 
#K-means cluster learning 



