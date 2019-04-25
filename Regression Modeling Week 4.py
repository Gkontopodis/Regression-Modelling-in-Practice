# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 20:20:07 2019

@author: Voltas
"""

import numpy
import pandas
import statsmodels.api as sm
import seaborn
import statsmodels.formula.api as smf

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)
nesarc = pandas.read_csv ('nesarc_pds.csv' , low_memory=False)

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

nesarc.columns = map(str.upper , nesarc.columns)

# Change my variables to numeric

nesarc['S3BQ1A5'] = pandas.to_numeric(nesarc['S3BQ1A5'], errors='coerce')
nesarc['MARP12ABDEP'] = pandas.to_numeric(nesarc['MARP12ABDEP'], errors='coerce') # Cannabis abuse/dependence
nesarc['COCP12ABDEP'] = pandas.to_numeric(nesarc['COCP12ABDEP'], errors='coerce') # Cocaine abuse/dependence
nesarc['ALCABDEPP12DX'] = pandas.to_numeric(nesarc['ALCABDEPP12DX'], errors='coerce') # Alcohol abuse/dependence
nesarc['HERP12ABDEP'] = pandas.to_numeric(nesarc['HERP12ABDEP'], errors='coerce') # Heroin abuse/dependence
nesarc['MAJORDEP12'] = pandas.to_numeric(nesarc['MAJORDEP12'], errors='coerce') # Major depression

# Subset my sample: ages 18-30

sub1=nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30)]

##############################################################################
# LOGISTIC REGRESSION
##############################################################################

# Binary cannabis abuse/dependence prior to the last 12 months

def CANDEPPR12 (x1):
   if x1['MARP12ABDEP']==1 or x1['MARP12ABDEP']==2 or x1['MARP12ABDEP']==3:
      return 1
   else: 
      return 0
sub1['CANDEPPR12'] = sub1.apply (lambda x1: CANDEPPR12 (x1), axis=1)
print (pandas.crosstab(sub1['MARP12ABDEP'], sub1['CANDEPPR12']))

## Logistic regression with cannabis abuse/dependence (explanatory) - major depression (response)

logreg1 = smf.logit(formula = 'MAJORDEP12 ~ CANDEPPR12', data = sub1).fit()
print (logreg1.summary())
# odds ratios
print ("Odds Ratios")
print (numpy.exp(logreg1.params))

# Odd ratios with 95% confidence intervals

params = logreg1.params
conf = logreg1.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))

# Binary cocaine abuse/dependence prior to the last 12 months

def COCDEPPR12 (x2):
   if x2['COCP12ABDEP']==1 or x2['COCP12ABDEP']==2 or x2['COCP12ABDEP']==3:
      return 1
   else: 
      return 0
sub1['COCDEPPR12'] = sub1.apply (lambda x2: COCDEPPR12 (x2), axis=1)
print (pandas.crosstab(sub1['COCP12ABDEP'], sub1['COCDEPPR12']))

## Logistic regression with cannabis and cocaine abuse/depndence (explanatory) - major depression (response)

logreg2 = smf.logit(formula = 'MAJORDEP12 ~ CANDEPPR12 + COCDEPPR12', data = sub1).fit()
print (logreg2.summary())

# Odd ratios with 95% confidence intervals

params = logreg2.params
conf = logreg2.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))

# Binary alcohol abuse/dependence prior to the last 12 months

def ALCDEPPR12 (x2):
   if x2['ALCABDEPP12DX']==1 or x2['ALCABDEPP12DX']==2 or x2['ALCABDEPP12DX']==3:
      return 1
   else: 
      return 0
sub1['ALCDEPPR12'] = sub1.apply (lambda x2: ALCDEPPR12 (x2), axis=1)
print (pandas.crosstab(sub1['ALCABDEPP12DX'], sub1['ALCDEPPR12']))

# Binary sedative abuse/dependence prior to the last 12 months

def HERDEPPR12 (x3):
   if x3['HERP12ABDEP']==1 or x3['HERP12ABDEP']==2 or x3['HERP12ABDEP']==3:
      return 1
   else: 
      return 0
sub1['HERDEPPR12'] = sub1.apply (lambda x3: HERDEPPR12 (x3), axis=1)
print (pandas.crosstab(sub1['HERP12ABDEP'], sub1['HERDEPPR12']))

## Logistic regression with alcohol abuse/depndence (explanatory) - major depression (response)

logreg3 = smf.logit(formula = 'MAJORDEP12 ~ HERDEPPR12', data = sub1).fit()
print (logreg3.summary())

# Odd ratios with 95% confidence intervals

print ("Odds Ratios")
params = logreg3.params
conf = logreg3.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))

## Logistic regression with cannabis and alcohol abuse/depndence (explanatory) - major depression (response)

logreg4 = smf.logit(formula = 'MAJORDEP12 ~ CANDEPPR12 + ALCDEPPR12 + COCDEPPR12', data = sub1).fit()
print (logreg4.summary())

# Odd ratios with 95% confidence intervals

print ("Odds Ratios")
params = logreg4.params
conf = logreg4.conf_int()
conf['OR'] = params
conf.columns = ['Lower CI', 'Upper CI', 'OR']
print (numpy.exp(conf))



