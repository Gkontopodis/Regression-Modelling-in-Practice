# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:52:07 2019

@author: Voltas
"""

import numpy
import pandas
import statsmodels.api as sm
import seaborn
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%.2f'%x)

nesarc = pandas.read_csv ('nesarc_pds.csv' , low_memory=False)

#Set PANDAS to show all columns in DataFrame
pandas.set_option('display.max_columns', None)
#Set PANDAS to show all rows in DataFrame
pandas.set_option('display.max_rows', None)

nesarc.columns = map(str.upper , nesarc.columns)

# Change my variables to numeric

nesarc['IDNUM'] =pandas.to_numeric(nesarc['IDNUM'], errors='coerce')
nesarc['S3BQ1A5'] = pandas.to_numeric(nesarc['S3BQ1A5'], errors='coerce')
nesarc['MAJORDEP12'] = pandas.to_numeric(nesarc['MAJORDEP12'], errors='coerce')
nesarc['AGE'] =pandas.to_numeric(nesarc['AGE'], errors='coerce')
nesarc['SEX'] = pandas.to_numeric(nesarc['SEX'], errors='coerce')
nesarc['S3BD5Q2E'] = pandas.to_numeric(nesarc['S3BD5Q2E'], errors='coerce')

# Current cannabis abuse criteria
nesarc['S3CD5Q14C9'] = pandas.to_numeric(nesarc['S3CD5Q14C9'], errors='coerce')
nesarc['S3CQ14A8'] = pandas.to_numeric(nesarc['S3CQ14A8'], errors='coerce')

# Longer period cannabis abuse criteria
nesarc['S3CD5Q14C3'] = pandas.to_numeric(nesarc['S3CD5Q14C3'], errors='coerce')

# Depressed because of cannabis effects wearing off
nesarc['S3CD5Q14C6C'] = pandas.to_numeric(nesarc['S3CD5Q14C6C'], errors='coerce')

# Sleep difficulties because of cannabis effects wearing off
nesarc['S3CD5Q14C6R'] = pandas.to_numeric(nesarc['S3CD5Q14C6R'], errors='coerce')

# Eat more because of cannabis effects wearing off
nesarc['S3CD5Q14C6H'] = pandas.to_numeric(nesarc['S3CD5Q14C6H'], errors='coerce')

# Feel nervous or anxious because of cannabis effects wearing off
nesarc['S3CD5Q14C6I'] = pandas.to_numeric(nesarc['S3CD5Q14C6I'], errors='coerce')

# Fast heart beat because of cannabis effects wearing off
nesarc['S3CD5Q14C6D'] = pandas.to_numeric(nesarc['S3CD5Q14C6D'], errors='coerce')

# Feel weak or tired because of cannabis effects wearing off
nesarc['S3CD5Q14C6B'] = pandas.to_numeric(nesarc['S3CD5Q14C6B'], errors='coerce')

# Withdrawal symptoms
nesarc['S3CD5Q14C6U'] = pandas.to_numeric(nesarc['S3CD5Q14C6U'], errors='coerce')


# Subset my sample: Cannabis users, ages 18-30

sub1=nesarc[(nesarc['AGE']>=18) & (nesarc['AGE']<=30) & (nesarc['S3BQ1A5']==1)]

############### Cannabis abuse/dependence criteria in the last 12 months (response variable) ###############

# Current cannabis abuse/dependence criteria #1 DSM-IV

def crit1 (row):
   if row['S3CD5Q14C9']==1 or row['S3CQ14A8'] == 1 :
      return 1
   elif row['S3CD5Q14C9']==2 and row['S3CQ14A8']==2 :
      return 0
sub1['crit1'] = sub1.apply (lambda row: crit1 (row),axis=1)
chk2 = sub1['crit1'].value_counts(sort=False, dropna=False)
print (chk2)
chk3 = sub1['S3CD5Q14C9'].value_counts(sort=False, dropna=False)
print (chk3)
chk4 = sub1['S3CQ14A8'].value_counts(sort=False, dropna=False)
print (chk4)
print (pandas.crosstab(sub1['S3CD5Q14C9'], sub1['S3CQ14A8']))

c1 = sub1['S3CD5Q14C6U'].value_counts(sort=False, dropna=False)
print (c1)

# Current 6 cannabis abuse/dependence sub-symptoms criteria #2 DSM-IV 

# Recode for summing (from 1,2 to 0,1)
recode1 = {1: 1, 2: 0}
sub1['S3CD5Q14C6C']=sub1['S3CD5Q14C6C'].replace(9, numpy.nan)
sub1['S3CD5Q14C6C']= sub1['S3CD5Q14C6C'].map(recode1)
sub1['S3CD5Q14C6R']=sub1['S3CD5Q14C6R'].replace(9, numpy.nan)
sub1['S3CD5Q14C6R']= sub1['S3CD5Q14C6R'].map(recode1)
sub1['S3CD5Q14C6H']=sub1['S3CD5Q14C6H'].replace(9, numpy.nan)
sub1['S3CD5Q14C6H']= sub1['S3CD5Q14C6H'].map(recode1)
sub1['S3CD5Q14C6I']=sub1['S3CD5Q14C6I'].replace(9, numpy.nan)
sub1['S3CD5Q14C6I']= sub1['S3CD5Q14C6I'].map(recode1)
sub1['S3CD5Q14C6D']=sub1['S3CD5Q14C6D'].replace(9, numpy.nan)
sub1['S3CD5Q14C6D']= sub1['S3CD5Q14C6D'].map(recode1)
sub1['S3CD5Q14C6B']=sub1['S3CD5Q14C6B'].replace(9, numpy.nan)
sub1['S3CD5Q14C6B']= sub1['S3CD5Q14C6B'].map(recode1)

# Check recode
chk1c = sub1['S3CD5Q14C6U'].value_counts(sort=False, dropna=False)
print (chk1c)

# Sum symptoms
sub1['CWITHDR_COUNT'] = numpy.nansum([sub1['S3CD5Q14C6C'], sub1['S3CD5Q14C6R'], 
              sub1['S3CD5Q14C6H'], sub1['S3CD5Q14C6I'],
              sub1['S3CD5Q14C6D'], sub1['S3CD5Q14C6B']], axis=0)

# Sum code check
chksum=sub1[['IDNUM','S3CD5Q14C6C', 'S3CD5Q14C6R', 'S3CD5Q14C6H', 
           'S3CD5Q14C6I', 'S3CD5Q14C6D', 'S3CD5Q14C6B', 'CWITHDR_COUNT']]
chksum.head(n=50)

chk1d = sub1['CWITHDR_COUNT'].value_counts(sort=False, dropna=False)
print (chk1d)

# Withdrawal symptoms in the last 12 months (yes/no)
def crit2 (row):
   if row['CWITHDR_COUNT']>=3 or row['S3CD5Q14C6U']==1:
      return 1
   elif row['CWITHDR_COUNT']<3 and row['S3CD5Q14C6U']!=1:
      return 0
sub1['crit2'] = sub1.apply (lambda row: crit2 (row),axis=1)
print (pandas.crosstab(sub1['CWITHDR_COUNT'], sub1['crit2']))


# Longer period cannabis abuse/dependence criteria #3 DSM-IV

sub1['S3CD5Q14C3']=sub1['S3CD5Q14C3'].replace(9, numpy.nan)
sub1['S3CD5Q14C3']= sub1['S3CD5Q14C3'].map(recode1)
  
chk1d = sub1['S3CD5Q14C3'].value_counts(sort=False, dropna=False)
print (chk1d)


# Current cannabis use cut down criteria #4 DSM-IV

sub1['S3CD5Q14C2'] = pandas.to_numeric(sub1['S3CD5Q14C2'], errors='coerce')   # Without success
sub1['S3CD5Q14C1'] = pandas.to_numeric(sub1['S3CD5Q14C1'], errors='coerce')   # More than once
def crit4 (row):
   if row['S3CD5Q14C2']==1 or row['S3CD5Q14C1'] == 1 :
      return 1
   elif row['S3CD5Q14C2']==2 and row['S3CD5Q14C1']==2 :
      return 0
sub1['crit4'] = sub1.apply (lambda row: crit4 (row),axis=1)
chk1e = sub1['crit4'].value_counts(sort=False, dropna=False)
print (chk1e)

# Current reduce of important/pleasurable activities criteria #5 DSM-IV

sub1['S3CD5Q14C10'] = pandas.to_numeric(sub1['S3CD5Q14C10'], errors='coerce')
sub1['S3CD5Q14C11'] = pandas.to_numeric(sub1['S3CD5Q14C11'], errors='coerce')
def crit5 (row):
   if row['S3CD5Q14C10']==1 or row['S3CD5Q14C11'] == 1 :
      return 1
   elif row['S3CD5Q14C10']==2 and row['S3CD5Q14C11']==2 :
      return 0
sub1['crit5'] = sub1.apply (lambda row: crit5 (row),axis=1)
chk1g = sub1['crit5'].value_counts(sort=False, dropna=False)
print (chk1g)

# Current cannbis use continuation despite knowledge of physical or psychological problem criteria #6 DSM-IV

sub1['S3CD5Q14C13'] = pandas.to_numeric(sub1['S3CD5Q14C13'], errors='coerce')
sub1['S3CD5Q14C12'] = pandas.to_numeric(sub1['S3CD5Q14C12'], errors='coerce')
def crit6 (row):
   if row['S3CD5Q14C13']==1 or row['S3CD5Q14C12'] == 1 :
      return 1
   elif row['S3CD5Q14C13']==2 and row['S3CD5Q14C12']==2 :
      return 0
sub1['crit6'] = sub1.apply (lambda row: crit6 (row),axis=1)
chk1h = sub1['crit6'].value_counts(sort=False, dropna=False)
print (chk1h)

# Cannabis abuse/dependence symptoms sum

sub1['CanDepSymptoms'] = numpy.nansum([sub1['crit1'], sub1['crit2'], sub1['S3CD5Q14C3'], 
              sub1['crit4'], sub1['crit5'],
              sub1['crit6']], axis=0 )
chk2 = sub1['CanDepSymptoms'].value_counts(sort=False, dropna=False)
print (chk2)


c1 = sub1["MAJORDEP12"].value_counts(sort=False, dropna=False)
print(c1)
c2 = sub1["AGE"].value_counts(sort=False, dropna=False)
print(c2)

############### Major depression diagnosis in the last 12 months (explanatory variable) ###############

# Major depression diagnosis

print('OLS regression model for the association between major depression diagnosis and cannabis depndence symptoms')
reg1 = smf.ols('CanDepSymptoms ~ MAJORDEP12', data=sub1).fit()
print (reg1.summary())

# Listwise deletion for calculating means for regression model observations

sub1 = sub1[['CanDepSymptoms', 'MAJORDEP12']].dropna()

# Group means & sd

print ("Mean")
ds1 = sub1.groupby('MAJORDEP12').mean()
print (ds1)
print ("Standard deviation")
ds2 = sub1.groupby('MAJORDEP12').std()
print (ds2)

# Bivariate bar graph

print('Bivariate bar graph for major depression diagnosis and cannabis depndence symptoms')
seaborn.factorplot(x="MAJORDEP12", y="CanDepSymptoms", data=sub1, kind="bar", ci=None)
plt.xlabel('Major Depression Diagnosis')
plt.ylabel('Mean Number of Cannabis Dependence Symptoms')


