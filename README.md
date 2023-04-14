# US Treasury Curve RV Analysis 
### Introduction, Value and Inspiration

  This project aims to parse through US treasuries historical data to generate meaningful insights to and visualise how the yield curve has moved historically. This can help traders contextualise the next movement, as well as benchmark their spread trades. 
  
  Read more on yield curve primers on the resources here: 
  1. Yield Curve Basics [LINK](https://www.investopedia.com/terms/y/yieldcurve.asp) 
  2. Spreads vs Butterfly Trade [LINK](https://www.clarusft.com/spreads-and-butterflies-what-is-trading/) 

  Thank you to Matteo Loria for being a great technical support during this project. 

### Data Source and Integrity 
  The data used in the this project was taken majorly from Quandl (now, nasdaq-data-link).
 
### Outcomes 

  First, we can take a look at how the yield curve has shifted in the past. This is important visualisation overall. 
  ![yield_curve_visualisation](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/Curve_Visualisation.png) 
  
  The most important value in this project came from deriving the Z-Value for respective tenors (e.g. 1y3y or 3y5y). This is how a spread trade makes money so it's important to know whether the curve has move with or against our favours in selected timeframes (7 days, 14 days and 1 month). The steps to derive these viz are: 
  1. Create a simple matrix calculation the spreads between all tenors
  2. Calculate the mean and standard deviation to use in the formula (z = (x-m)/u) 
  3. Visualise using seaborn and applying heatmap gradient to help with quick spotting 

  Example intepretation (7 days rolling): 3s5s moved by 2 Z's meaning spread has widened compared to historical average. This means that the curve has steepend.

  ![7 days](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/7d_rolling.png) 
  ![14 days](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/14d_rolling.png)
  ![1_month](https://github.com/phuongnd1112/Trading-the-US-Historical-RV-Yield/blob/main/1mo_rolling.png) 
