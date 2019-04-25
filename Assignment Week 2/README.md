# Basic Linear Regression Model

## Preview
The data was provided by the National Epidemiological Survey on Alcohol and Related Conditions (NESARC), which was conducted in a random sample of 43,093 U.S. adults and designed to determine the magnitude of alcohol use and psychiatric disorders. The data analytic subset, examined in this study, includes individuals aged between 18 and 30 years old who reported using cannabis at least once in their life (N=2,412). This assignment aims to evaluate the association between major depression diagnosis in the last 12 months (categorical explanatory variable) and cannabis dependence symptoms (quantitative response variable) during the same period, using a linear regression model.

## Variables
### Explanatory
![datascreenshot](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/sc7.png)

Major depression diagnosis **(MAJORDEP12)** is a 2-level categorical variable (0=“No” , 1=“Yes”). The “No” category was initially coded “0”, thus there was no need for recode.

#### Frequency table of major depression diagnosis in cannabis users, ages 18-30
![counts](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/out1.png)
![percentages](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/out2.png)

### Response
Cannabis dependence symptoms (CanDepSymptoms) is a quantitative variable which I created for the purpose of the assignment. This variable was coded to represent the sum of 6 criteria:

1. Current cannabis abuse/dependence criteria, variables: **S3CD5Q14C9** , **S3CD5Q14C9**
2. Longer period cannabis abuse/dependence criteria, variable: **S3CD5Q14C3**
3. Cannabis abuse/dependence sub-symptom criteria, which are: 
     * Feel depressed because of cannabis effects wearing off, variable: **S3CD5Q14C6C**
     * Face sleeping difficulties because of cannabis effects wearing off, variable: **S3CD5Q14C6R**
     * Eat more because of cannabis effects wearing off, variable: **S3CD5Q14C6H**
     * Feel nervous or anxious because of cannabis effects wearing off, variable: **S3CD5Q14C6I**
     * Have fast heart beat because of cannabis effects wearing off, variable: **S3CD5Q14C6D**
     * Feel weak or tired because of cannabis effects wearing off, variable: **S3CD5Q14C6B**
4. Current cannabis use cut down criteria, variables: **S3CD5Q14C2** , **S3CD5Q14C1**     
5. Current reduce of important/pleasurable activities criteria, variables: **S3CD5Q14C10** , **S3CD5Q14C11**
6. Current cannabis use continuation despite knowledge of physical or psychological problem criteria, variables: **S3CD5Q14C13** , **S3CD5Q14C12**

## Measures
I used ols function in order to estimate the regression equation and examine if major depression is correlated with cannabis dependence symptoms. Therefore, the F-statistic, P-value and parameter estimates (a.k.a. coefficients or beta weights) were calculated. In addition, the mean and the standard deviation were evaluated and the results were visualized with a bivariate bar graph.

## Linear Regression Analysis Results
![olsfunc](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/out3.png)

The linear regression model presented above aims to examine the association between major depression diagnosis in the last 12 months (categorical explanatory variable) and cannabis dependence symptoms (quantitative response variable), among U.S. adults aged between 18 and 30 years old. The number of observations that had valid data on both the response and explanatory variables and were therefore included in this analysis, was 2,412. The F-statistic is 60.34 and the P-value is 1.17e-14 (written in scientific notation). The P-value is considerably less than our alpha level of 0.05, which indicates that we can reject the null hypothesis and conclude that major depression diagnosis is significantly associated with cannabis dependence symptoms. In addition, the coefficient for major depression diagnosis is 0.38, and the intercept is 0.39. The P-value for our explanatory variable, in association with the response variable is p<0.0001 and the R-squared value, which is the proportion of the variance in cannabis dependence symptoms that can be explained by the major depression diagnosis, is significantly low at 2.4%.

### Model Regression Equation
![eq](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/eq.gif)

### Bar Chart
![graph](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%202/Output%20Analysis/out8.png)

The bivariate bar graph presented above illustrates the association between major depression, diagnosed in the last 12 months (explanatory variable) and cannabis dependence symptoms (response variable), in U.S. adults aged from 18 to 30 years old. The “No” category of major depression diagnosis is coded with “0” and the “Yes” is coded with “1”. As we can see, the individuals diagnosed with major depression in the last 12 months appeared to have marginally double cannabis dependence symptoms (mean = 0.77), compared to those who did not meet the criteria for this disorder (mean = 0.39). Therefore, major depression diagnosis is significantly associated with cannabis dependence symptoms. 

