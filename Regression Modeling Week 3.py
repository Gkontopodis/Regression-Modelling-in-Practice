# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 14:59:00 2019

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
nesarc['MAJORDEP12'] = pandas.to_numeric(nesarc['MAJORDEP12'], errors='coerce') # Major depression
nesarc['AGE'] =pandas.to_numeric(nesarc['AGE'], errors='coerce')
nesarc['SEX'] = pandas.to_numeric(nesarc['SEX'], errors='coerce')
nesarc['S3BD5Q2E'] = pandas.to_numeric(nesarc['S3BD5Q2E'], errors='coerce') # Cannabis use frequency
nesarc['S3BQ4'] = pandas.to_numeric(nesarc['S3BQ4'], errors='coerce') # Quantity of joints per day
nesarc['GENAXDX12'] = pandas.to_numeric(nesarc['GENAXDX12'], errors='coerce') # General anxiety
nesarc['S3BD5Q2F'] = pandas.to_numeric(nesarc['S3BD5Q2F'], errors='coerce') # Age when began using cannabis the most
nesarc['DYSDX12'] = pandas.to_numeric(nesarc['DYSDX12'], errors='coerce') # Dysthymia
nesarc['SOCPDX12'] = pandas.to_numeric(nesarc['SOCPDX12'], errors='coerce') # Social phobia
nesarc['S3BD5Q2GR'] = pandas.to_numeric(nesarc['S3BD5Q2GR'], errors='coerce') # Cannabis use duration (weeks)
nesarc['S3CD5Q15C'] = pandas.to_numeric(nesarc['S3CD5Q15C'], errors='coerce') # Cannabis dependence
nesarc['S3CD5Q13B'] = pandas.to_numeric(nesarc['S3CD5Q13B'], errors='coerce') # Cannabis abuse

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


# Sum symptoms
sub1['CWITHDR_COUNT'] = numpy.nansum([sub1['S3CD5Q14C6C'], sub1['S3CD5Q14C6R'], 
              sub1['S3CD5Q14C6H'], sub1['S3CD5Q14C6I'],
              sub1['S3CD5Q14C6D'], sub1['S3CD5Q14C6B']], axis=0)

# Sum code check
chksum=sub1[['IDNUM','S3CD5Q14C6C', 'S3CD5Q14C6R', 'S3CD5Q14C6H', 
           'S3CD5Q14C6I', 'S3CD5Q14C6D', 'S3CD5Q14C6B', 'CWITHDR_COUNT']]
chksum.head(n=50)

# Withdrawal symptoms in the last 12 months (yes/no)
def crit2 (row):
   if row['CWITHDR_COUNT']>=3 or row['S3CD5Q14C6U']==1:
      return 1
   elif row['CWITHDR_COUNT']<3 and row['S3CD5Q14C6U']!=1:
      return 0
sub1['crit2'] = sub1.apply (lambda row: crit2 (row),axis=1)

# Longer period cannabis abuse/dependence criteria #3 DSM-IV

sub1['S3CD5Q14C3']=sub1['S3CD5Q14C3'].replace(9, numpy.nan)
sub1['S3CD5Q14C3']= sub1['S3CD5Q14C3'].map(recode1)

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

# Cannabis abuse/dependence symptoms sum

sub1['CanDepSymptoms'] = numpy.nansum([sub1['crit1'], sub1['crit2'], sub1['S3CD5Q14C3'], 
              sub1['crit4'], sub1['crit5'],
              sub1['crit6']], axis=0 )
chk2 = sub1['CanDepSymptoms'].value_counts(sort=False, dropna=False)

##############################################################################
# MULTIPLE REGRESSION & CONFIDENCE INTERVALS
##############################################################################

sub2 = sub1[['S3BQ4', 'S3BD5Q2F', 'DYSDX12', 'MAJORDEP12', 'CanDepSymptoms', 'SOCPDX12', 'GENAXDX12', 'S3BD5Q2GR']].dropna()

# Centre the quantity of joints smoked per day and age when they began using cannabis, quantitative variables
sub1['numberjosmoked_c'] = (sub1['S3BQ4'] - sub1['S3BQ4'].mean())
sub1['agebeganuse_c'] = (sub1['S3BD5Q2F'] - sub1['S3BD5Q2F'].mean())
sub1['canuseduration_c'] = (sub1['S3BD5Q2GR'] - sub1['S3BD5Q2GR'].mean())

# Linear regression analysis

print('OLS regression model for the association between major depression diagnosis and cannabis depndence symptoms')
reg1 = smf.ols('CanDepSymptoms ~ MAJORDEP12', data=sub1).fit()
print (reg1.summary())

print('OLS regression model for the association of majord depression diagnosis and smoking quantity with cannabis dependence symptoms')
reg2 = smf.ols('CanDepSymptoms ~ MAJORDEP12 + DYSDX12', data=sub1).fit()
print (reg2.summary())

reg3 = smf.ols('CanDepSymptoms ~ MAJORDEP12 + agebeganuse_c + numberjosmoked_c + canuseduration_c + GENAXDX12 + DYSDX12 + SOCPDX12', data=sub1).fit()
print (reg3.summary())

####################################################################################
# POLYNOMIAL REGRESSION
####################################################################################

# First order (linear) scatterplot
scat1 = seaborn.regplot(x="S3BQ4", y="CanDepSymptoms", scatter=True, data=sub1)
plt.ylim(0, 6)
plt.xlabel('Quantity of joints')
plt.ylabel('Cannabis dependence symptoms')

# Fit second order polynomial
scat1 = seaborn.regplot(x="S3BQ4", y="CanDepSymptoms", scatter=True, order=2, data=sub1)
plt.ylim(0, 6)
plt.xlabel('Quantity of joints')
plt.ylabel('Cannabis dependence symptoms')

# Linear regression analysis
reg4 = smf.ols('CanDepSymptoms ~ numberjosmoked_c', data=sub1).fit()
print (reg4.summary())

reg5 = smf.ols('CanDepSymptoms ~ numberjosmoked_c + I(numberjosmoked_c**2)', data=sub1).fit()
print (reg5.summary())

####################################################################################
# EVALUATING MODEL FIT
####################################################################################
recode1 = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1}       # Dictionary with details of frequency variable reverse-recode
sub1['CUFREQ'] = sub1['S3BD5Q2E'].map(recode1)     # Change variable name from S3BD5Q2E to CUFREQ

sub1['CUFREQ_c'] = (sub1['CUFREQ'] - sub1['CUFREQ'].mean())

# Adding frequency of cannabis use
reg6 = smf.ols('CanDepSymptoms ~ numberjosmoked_c + I(numberjosmoked_c**2) + CUFREQ_c', 
               data=sub1).fit()
print (reg6.summary())

# Q-Q plot for normality
fig1=sm.qqplot(reg6.resid, line='r')
print (fig1)

# Simple plot of residuals
stdres=pandas.DataFrame(reg6.resid_pearson)
fig2=plt.plot(stdres, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')

# Additional regression diagnostic plots
fig3 = plt.figure(figsize=(12,8))
fig3 = sm.graphics.plot_regress_exog(reg6,  "CUFREQ_c", fig=fig3)

# leverage plot
fig4 = plt.figure(figsize=(36,24))
fig4=sm.graphics.influence_plot(reg6, size=2)
print(fig4)
































