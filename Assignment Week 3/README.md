# Multiple Regression Model

### Analysis

![out1](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out1.png)
![out2](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out2.png)

The multiple regression analysis aims to evaluate multiple predictors of the quantitative response variable, number of cannabis dependence symptoms (**CanDepSymptoms**). The primary explanatory variable is major depression diagnosis, in the last 12 months (**MAJORDEP12**), while the confounding factors are:         
* **agebeganuse_c**: Centered quantitative variable, which represents the age when individuals began using cannabis the most (values 5-64. Age).
* **numberjosmoked_c**:  Centered quantitative variable, which represents the number of joints smoked per day when using cannabis the most (values 1-98. Joints). 
* **canuseduration_c**:  Centered quantitative variable, which represents the duration (in weeks) individuals used cannabis the most (values 1-2818. Weeks).
* **GENAXDX12**: Categorical variable, which represents the diagnosis of general anxiety in the last 12 months (0.=“No”, 1.=“Yes”).
* **DYSDX12**:  Categorical variable, which represents the diagnosis of dysthymia in the last 12 months (0.=“No”, 1.=“Yes”).
* **SOCPDX12**:  Categorical variable, which represents the diagnosis of social phobia in the last 12 months (0.=“No”, 1.=“Yes”).  

After adjusting the potential confounding factors, major depression (Beta=0.25, p=0.0001) was significantly and positively associated with number of cannabis dependence symptoms. The R-squared value was extremely small at 0.047 and F-statistic value is equal to 16.88. For the confounding variables:
* Age when began using cannabis the most was not significantly associated with cannabis dependence symptoms and the null hypothesis cannot be rejected (Beta=-0.03, p=0.18).
* Number of joints smoked per day was significantly associated with cannabis dependence symptoms, such that the larger quantity reported a greater number of cannabis dependence symptoms (Beta= 0.003, p=0.008). 
* Duration of cannabis use was not significantly associated with cannabis dependence symptoms and the null hypothesis cannot be rejected (Beta=9.4e-06, p=0.56).
* General anxiety diagnosis was not significantly associated with cannabis dependence symptoms and the null hypothesis cannot be rejected (Beta=0.18, p=0.07).
* Dysthymia diagnosis was significantly associated with cannabis dependence symptoms (Beta= 0.43, p=0.0001). 
* Social phobia diagnosis was significantly associated with cannabis dependence symptoms (Beta= 0.31, p=0.0001). 

### Report

To evaluate if the additional explanatory variables confounded the relationship between major depression diagnosis (primary explanatory variable) and cannabis dependence symptoms (response variable), I added the variables to my model one at a time. As a result, none of this variables confounded the association, since every time I added each predictor the p-value of major depression remained significant, at 0.0001. Therefore, the results of the multiple regression analysis for these adjusted potential confounding variables, supported my initial hypothesis.

### Polynomial Regression

![out3](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out3.png)
![out4](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out4.png)
![out5](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out5.png)

The second multiple regression analysis examines the association between the quantitative response variable, number of cannabis dependence symptoms (**CanDepSymptoms**) and the centered quantitative explanatory variable, number of joints smoked per day when using the most (**numberjosmoked_c**). A second order polynomial of number of joints variable (**’numberjosmoked_c^2**) was added to the regression equation in order to improve the fit of the model and capture the curve of linear relationship that was evident in the scatter plot. In addition, the recoded variable (**CUFREQ**) which represents the frequency of cannabis use (values 1-10, 1.=“Once a year”, 10.=“Every day”), was included to the model as a potential confounding factor. There is also a show that coefficients for the linear, and quadratic variables, remain significant after adjusting for frequency of cannabis use rate.   

If we look at the results, it is noticeable that the value for the linear term for number of joints is 0.05, and the p value is less than 0.0001. In addition, the quadratic term is negative (-0.0006) and the p value is also significant (0.0001). The R square increases from 0.003 to 0.18., which means that adding the quadratic term for cannabis joints, increase the amount of variability in cannabis dependence symptoms that can be explained by cannabis use quantity from 0.3% to 18%. For the frequency of cannabis use the coefficient is equal to 0.09 and the p-value is significantly small, at 0.0001.

![graph1](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out6.png)

## Diagnostic Plots

### Q to Q Plot

![graph2](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out7.png)

This qq-plot evaluates the assumption that the residuals from our reggression model are normally distributed. A qq-plot, plots the quantiles of the residuals that we would theoretically see if the residuals followed a normal distribution, against the quantiles for the residuals estimated from the reggression model. It is noticeable that the residuals generally deviate from a straight line, especially at higher quantiles. This indicates that our residuals did not follow perfect normal distribution. This could mean that the curvilinear association that we observed in our scatter plot may not be fully estimated by the quadratic cannabis joints variable. Therefore, there might be other explanatory variables that could improve estimation of the observed curvilinearity. 

### Plot of standardized residuals for all observations

![graph3](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out8.png)

To evaluate the overall fit of the predicted values of the response variable to the observed values and to look for outliers, I created a plot for the standardized residuals of each observation. As we can see, most of the residuals fall between -2 and 2, but many of them fall also above 2. This indicates that we have several outliers, basically above the mean of 0. Furthermore, some of these outliers fall above 4 (extreme outliers) which suggests that the fit of the model is relatively poor and could be improved. 

### Regression plots for frequency of cannabis use

![graph4](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out9.png)

The plot in the upper right hand corner shows the residuals for each observation at different values of cannabis use frequency rate. There is clearly a funnel shaped pattern to the residuals where we can see that the absolute values of the them are small at lower values of frequency use rate, but then they start to get larger at higher levels. This indicates that this model does not predict cannabis dependence symptoms as well for individuals who have either high or low levels of cannabis use frequency rate. But is particularly worse predicting dependence symptoms for individuals with high frequency of cannabis use. 

The partial regression residual plot, in the lower left hand corner, attempts to show the effect of adding cannabis use frequency rate as an additional explanatory variable to the model. For the frequency use rate variable, the values in the scatter plot are two sets of residuals. The residuals from a model predicting the cannabis dependence symptoms response from the other explanatory variables, excluding frequency of use, are plotted on the vertical access, and the residuals from the model predicting frequency of use from all the other explanatory variables are plotted on the horizontal access.What this means is that the partial regression plot shows the relationship between the response variable and specific explanatory variable, after controlling for the other explanatory variables. The residuals are spread out in a random pattern around the partial regression line and many of the residuals are pretty far from this line, indicating a great deal of cannabis dependence symptoms prediction error. Although cannabis use frequency rate shows a statistically significant association with cannabis dependence symptoms, this association is pretty weak after controlling for the number of joints smoked.

### Leverage plot

![graph5](https://github.com/Gkontopodis/Regression-Modelling-in-Practice/blob/master/Assignment%20Week%203/Output%20-%20Graphs/out10.png)

The leverage plot attempts to identify observations that have an unusually large influence on the estimation of the predicted value of the response variable, cannabis dependence symptoms, or that are outliers, or both. We can see in the leverage plot is that we have a several outliers, contents that have residuals greater than 2 or less than -2. We’ve already identified some of these outliers in previous plots, but the plot also tells us which outliers have small or close to zero leverage values, meaning that although they are outlying observations, they do not have an undue influence on the estimation of the regression model.

 
