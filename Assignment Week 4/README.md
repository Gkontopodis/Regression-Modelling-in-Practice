# Logistic Regression  Model

## Preview

This assignment aims to examine the association of potential drug abuse/dependence prior to the last 12 months with major depression diagnosis in the last 12 months. among US adults aged from 18 to 30 years old (N=9535). All four explanatory variables were 4-level categorical and they were binned into 2 categories (0.=“No abuse/dependence, 1.=“Drug abuse/dependence”) for the purpose of these logistic models. More specifically, cannabis abuse/dependence (**CANDEPPR12**) is the primary explanatory variable and the potential confounding factors were cocaine (**COCDEPPR12**), heroine (**HERDEPPR12**) and alcohol (**ALCDEPPR12**). The response variable is major depression (**MAJORDEP12**) diagnosed in the last 12 months, which is categorical binary variable (0.=“No”, 1.=“Yes”). Therefore, we can evaluate if a specific drug abuse/dependence issue during the period prior to the last 12 months, is positively correlated with depression diagnosis in the last 12 months. 

## Results

![out1](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%204/Results/out1.png)
![out2](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%204/Results/out2.png)

The logistic regression model presented above illustrates the association of cannabis and cocaine abuse/dependence issue prior to the last 12 months with major depression, diagnosed in the last 12 months. The number of observations is 9535 (18-30) and the regression is significant at a P value of less than 0.0001 for cannabis and 0.001 for cocaine. The odds of having major depression were 2.5 times higher for participants with cannabis abuse/dependence than for participants without abuse/dependence (OR=2.59, 95% CI = 2.17-3.10, p=.0001). For cocaine the odds of having major depression were more than 1.7 times higher for individuals with cocaine abuse/dependence than for individuals without   abuse/dependence (OR=1.73, 95% CI = 1.25-2.40, p=.001).

![out3](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%204/Results/out3.png)

On the other hand, heroine’s relationship with major depression was not significant, with a p-value at 0.079 which is more than 0.05. Thus, the null hypothesis cannot be rejected.

![out3](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%204/Results/out4.png)

After adjusting for potential confounding factors alcohol and cocaine abuse/dependence, the odds of having depression were slightly more double for participants with cannabis issues than for participants without cannabis issues (OR=2.11, 95% CI = 1.74-2.55, p=.0001). Alcohol appeared to be also positively correlated with major depression, since alcoholic individuals had 1.5 times higher odds of getting diagnosed with this psychiatric disorder (OR=1.5, 95% CI = 1.32-1.79, p=.0001). Cocaine’s abuse/dependence odds seemed to be very close to alcohol  (OR=1.54, 95% CI = 1.11-2.14, p=.01). 

## Summary

The logistic regression model revealed that cannabis, cocaine and alcohol were positively correlated with major depression, while heroine was not. Cannabis dependence was my primary explanatory variable and its significance appeared to remain steady when adding potential predictors (alcohol and cocaine) to the model. Therefore, there was no evidence of confounding for the association between my primary explanatory variable and the response variable. The results support my initial hypothesis.
