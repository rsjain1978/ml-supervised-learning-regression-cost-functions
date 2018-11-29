import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def gradient_descent(X,Y):
     iterations = 10000
     learning_factor = 0.001
     size = len(X)
     theta0 = 0
     theta1 = 0

     i = 0
     while (i < iterations):
        j = 0
        mse = 0
        #iterate over X and Y & calculate MSE
        while (j < size):
             mse = mse + pow((theta0+theta1*X[j]-Y[j]),2)      
             j=j+1
        print ('theta0 is {}, theta1 is {}, mse is {} after iteration {}'.format(theta0, theta1, mse, i))
        
        j=0
        d_theta0=0
        #iterate over X and Y & calculate theta0
        while (j < size):
            d_theta0 = d_theta0 + (theta0+theta1*X[j]-Y[j])
            j=j+1
        d_theta0=d_theta0/size
        theta0=theta0-learning_factor*d_theta0

        j=0
        d_theta1=0
        #iterate over X and Y & calculate theta0
        while (j < size):
            d_theta1 = d_theta1 + (theta0+theta1*X[j]-Y[j])*X[j]
            j=j+1
        d_theta1=d_theta1/size
        theta1=theta1-learning_factor*d_theta1

        i = i+1
      
     predicted_y = theta1*55+theta0
     print ('Predicted value of X=55 would be {}'.format(predicted_y))


X = np.array([10,20,30,40,50,60])
Y = np.array([23,33,43,53,63,73])

gradient_descent (X, Y)

#theta0 is 11.105340424363877, theta1 is 1.0437200477822675, mse is 4.142001891124454 after iteration 9999
#Predicted value of X=55 would be 68.50984495942348