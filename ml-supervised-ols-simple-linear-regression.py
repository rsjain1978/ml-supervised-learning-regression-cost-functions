import numpy as np
import pandas as pd
import math
import statistics as stats

# m = 1/n*(Sum((xi-mean(x))*(yi-mean(y)))/ Sum((xi-mean(x))^2))
# b = mean(y) - m*mean(x)
def generate_coeffecients_intercept(X,Y):
    n = len(X)

    x_mean = stats.mean(X)
    y_mean = stats.mean(Y)

    m = 0
    i = 0
    while (i<n):
        m =  m + (X[i]-x_mean)*(Y[i]-y_mean)/pow((x_mean-X[i]),2)
        i=i+1
    m = m/n
    b = y_mean - m*x_mean

    print ('Value of m is {} and b is {}'.format(m,b))
    predicted_y = m*55+b
    print ('Predicted value of X=55 would be {}'.format(predicted_y))


X = np.array([10,20,30,40,50,60])
Y = np.array([23,33,43,53,63,73])
generate_coeffecients_intercept(X,Y)