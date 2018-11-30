import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

def gradient_descent(X,Y):
     iterations = 14000
     learning_factor = 0.0006
     size = len(X)
     theta0 = 0
     theta1 = 0
     mse = 0
     i = 0

     while (i < iterations):

        y_predicted = (theta0 + theta1*X)
        d_theta0 = (1/size)*sum(y_predicted-Y)
        d_theta1 = (1/size)*sum((y_predicted-Y)*X)
        
        tmp_theta0 = theta0 - learning_factor*d_theta0
        tmp_theta1 = theta1 - learning_factor*d_theta1
        
        theta0 = tmp_theta0
        theta1 = tmp_theta1
        
        mse = (1/size)*sum(pow((y_predicted-Y),2))
        print ('Theta0 is {}, Theta1 is {}, MSE is {}, Iteration is :{}'.format(theta0, theta1, mse, i))k
        
        i = i+1
      
     predicted_y = theta1*55+theta0
     print ('Predicted value of X=55 would be {}'.format(predicted_y))


X = np.array([10,20,30,40,50,60])
Y = np.array([23,33,43,53,63,73])

gradient_descent (X, Y)