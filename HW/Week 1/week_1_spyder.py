"""
Created on Tue Jan 23 11:35:09 2024

@author: dev46

Model Docstring: This model created a fucntion that turn a numpy array into 
a linear regression and plot the model in matplot
"""
import numpy as np
import matplotlib.pyplot as plt
X = np.arange(0,10,.5)

def linear_function(x_values):
    """"
    Docstring: linear_function(X)
    
    X: a Numpy array
    """
    m_value=4
    b_value=3
    y_values=m_value*x_values+b_value
    plt.scatter(x_values,y_values)
linear_function(X)
