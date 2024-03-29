#import libraries
install.packages('rmgarch', repos = "http://cran.us.r-project.org")
library(rmgarch)
#import the dataset we compute use python
returns <- read.csv("~/Desktop/returns.csv")
View(returns)
#model specifications
#GARCH(1,1)
garch11.spec = ugarchspec(mean.model = list(armaOrder = c(0,0)),
                          variance.model = list(garchOrder = c(1,1),model = "sGARCH"),
                          distribution.model = "norm")
garch11.spec

'''
*---------------------------------*
*       GARCH Model Spec          *
*---------------------------------*
  
  Conditional Variance Dynamics 	
------------------------------------
  GARCH Model		: sGARCH(1,1)
Variance Targeting	: FALSE 

Conditional Mean Dynamics
------------------------------------
  Mean Model		: ARFIMA(0,0,0)
Include Mean		: TRUE 
GARCH-in-Mean		: FALSE 

Conditional Distribution
------------------------------------
  Distribution	:  norm 
Includes Skew	:  FALSE 
Includes Shape	:  FALSE 
Includes Lambda	:  FALSE 
'''
n<-dim(returns)[2]

#DCC(1,1) with GARCH(1,1) constructed above
dcc.garch11.spec = dccspec(uspec = multispec(replicate(n,garch11.spec)),
                           dccOrder = c(1,1),
                           distribution="mvnorm")
dcc.garch11.spec 

'''
*------------------------------*
*       DCC GARCH Spec         *
*------------------------------*
Model          :  DCC(1,1)
Estimation     :  2-step
Distribution   :  mvnorm
No. Parameters :  17
No. Series     :  3
'''

# model estimation
result = dccfit(spec=dcc.garch11.spec, data=na.omit(returns))
result

'''
*---------------------------------*
*          DCC GARCH Fit          *
*---------------------------------*

Distribution         :  mvnorm
Model                :  DCC(1,1)
No. Parameters       :  17
[VAR GARCH DCC UncQ] : [0+12+2+3]
No. Series           :  3
No. Obs.             :  1005
Log-Likelihood       :  -4889.521
Av.Log-Likelihood    :  -4.87 

Optimal Parameters
-----------------------------------
               Estimate  Std. Error  t value Pr(>|t|)
[AAPL].mu      0.123569    0.046497  2.65760 0.007870
[AAPL].omega   0.225659    0.088530  2.54895 0.010805
[AAPL].alpha1  0.128393    0.035263  3.64103 0.000272
[AAPL].beta1   0.780760    0.052609 14.84074 0.000000
[GOOG].mu      0.080476    0.042767  1.88174 0.059872
[GOOG].omega   0.193072    0.161134  1.19820 0.230838
[GOOG].alpha1  0.187833    0.126945  1.47964 0.138969
[GOOG].beta1   0.747919    0.154264  4.84831 0.000001
[MSFT].mu      0.121999    0.044221  2.75883 0.005801
[MSFT].omega   0.014938    0.092794  0.16098 0.872109
[MSFT].alpha1  0.024745    0.074276  0.33314 0.739025
[MSFT].beta1   0.969867    0.109462  8.86033 0.000000
[Joint]dcca1   0.034478    0.013725  2.51197 0.012006
[Joint]dccb1   0.843667    0.038480 21.92490 0.000000

Information Criteria
---------------------
                   
Akaike       9.7642
Bayes        9.8473
Shibata      9.7637
Hannan-Quinn 9.7958


Elapsed time : 2.838903 
'''

#get the conditional covariance,conditional correlation, portfolio plot with conditional density VaR limit
plot(result)

#calculate five-step ahead forecast
forecasts <- dccforecast(result, n.ahead = 5)
forecasts

'''
*---------------------------------*
*       DCC GARCH Forecast        *
*---------------------------------*

Distribution         :  mvnorm
Model                :  DCC(1,1)
Horizon              :  5
Roll Steps           :  0
-----------------------------------

0-roll forecast: 
, , 1

       [,1]   [,2]   [,3]
[1,] 1.0000 0.6456 0.6625
[2,] 0.6456 1.0000 0.7453
[3,] 0.6625 0.7453 1.0000

, , 2

       [,1]   [,2]   [,3]
[1,] 1.0000 0.6278 0.6453
[2,] 0.6278 1.0000 0.7340
[3,] 0.6453 0.7340 1.0000

, , 3

       [,1]   [,2]   [,3]
[1,] 1.0000 0.6121 0.6302
[2,] 0.6121 1.0000 0.7241
[3,] 0.6302 0.7241 1.0000

, , 4

       [,1]   [,2]   [,3]
[1,] 1.0000 0.5983 0.6169
[2,] 0.5983 1.0000 0.7154
[3,] 0.6169 0.7154 1.0000

, , 5

       [,1]   [,2]   [,3]
[1,] 1.0000 0.5862 0.6053
[2,] 0.5862 1.0000 0.7078
[3,] 0.6053 0.7078 1.0000
'''

#assign the forecast
names(forecasts@mforecast)
'[1] "H"    "R"    "Q"    "Rbar" "mu" '

#conditional covariance matrix
forecasts@mforecast$H

'''
[[1]]
, , 1

         [,1]     [,2]     [,3]
[1,] 6.996757 4.237756 4.018266
[2,] 4.237756 6.157358 4.240759
[3,] 4.018266 4.240759 5.257858

, , 2

         [,1]     [,2]     [,3]
[1,] 6.586779 3.931634 3.792690
[2,] 3.931634 5.954830 4.102074
[3,] 3.792690 4.102074 5.244462

, , 3

         [,1]     [,2]     [,3]
[1,] 6.214045 3.663597 3.593009
[2,] 3.663597 5.765315 3.976738
[3,] 3.593009 3.976738 5.231138

, , 4

         [,1]     [,2]     [,3]
[1,] 5.875174 3.428138 3.415793
[2,] 3.428138 5.587975 3.863163
[3,] 3.415793 3.863163 5.217885

, , 5

         [,1]     [,2]     [,3]
[1,] 5.567088 3.220645 3.258122
[2,] 3.220645 5.422030 3.759978
[3,] 3.258122 3.759978 5.204704
'''

#conditional correlation matrix
forecasts@mforecast$R

'''
[[1]]
, , 1

          [,1]      [,2]      [,3]
[1,] 1.0000000 0.6456399 0.6624999
[2,] 0.6456399 1.0000000 0.7453186
[3,] 0.6624999 0.7453186 1.0000000

, , 2

          [,1]      [,2]      [,3]
[1,] 1.0000000 0.6277718 0.6452980
[2,] 0.6277718 1.0000000 0.7340376
[3,] 0.6452980 0.7340376 1.0000000

, , 3

          [,1]      [,2]      [,3]
[1,] 1.0000000 0.6120811 0.6301922
[2,] 0.6120811 1.0000000 0.7241313
[3,] 0.6301922 0.7241313 1.0000000

, , 4

          [,1]      [,2]      [,3]
[1,] 1.0000000 0.5983024 0.6169272
[2,] 0.5983024 1.0000000 0.7154322
[3,] 0.6169272 0.7154322 1.0000000

, , 5

          [,1]      [,2]      [,3]
[1,] 1.0000000 0.5862027 0.6052785
[2,] 0.5862027 1.0000000 0.7077931
[3,] 0.6052785 0.7077931 1.0000000
'''

# proxy correlation process
forecasts@mforecast$Q

'''
[[1]]
, , 1

          [,1]      [,2]      [,3]
[1,] 1.2215344 0.8006877 0.8309965
[2,] 0.8006877 1.2590411 0.9491229
[3,] 0.8309965 0.9491229 1.2880154

, , 2

          [,1]      [,2]      [,3]
[1,] 1.2215344 0.8006877 0.8309965
[2,] 0.8006877 1.2590411 0.9491229
[3,] 0.8309965 0.9491229 1.2880154

, , 3

          [,1]      [,2]      [,3]
[1,] 1.2215344 0.8006877 0.8309965
[2,] 0.8006877 1.2590411 0.9491229
[3,] 0.8309965 0.9491229 1.2880154

, , 4

          [,1]      [,2]      [,3]
[1,] 1.2215344 0.8006877 0.8309965
[2,] 0.8006877 1.2590411 0.9491229
[3,] 0.8309965 0.9491229 1.2880154

, , 5

          [,1]      [,2]      [,3]
[1,] 1.2215344 0.8006877 0.8309965
[2,] 0.8006877 1.2590411 0.9491229
[3,] 0.8309965 0.9491229 1.2880154
'''

# conditional mean forecasts
forecasts@mforecast$mu

'''
, , 1

          [,1]       [,2]      [,3]
[1,] 0.1235695 0.08047593 0.1219989
[2,] 0.1235695 0.08047593 0.1219989
[3,] 0.1235695 0.08047593 0.1219989
[4,] 0.1235695 0.08047593 0.1219989
[5,] 0.1235695 0.08047593 0.1219989
'''
plot(forecasts)
