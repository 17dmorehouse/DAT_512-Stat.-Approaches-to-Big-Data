"""
Created on Tue Jan 23 11:35:09 2024

@author: dev46

Model Docstring: This model created a fucntion that turn a numpy array into 
a linear regression and plot the model in matplot
"""
import numpy as np
import matplotlib.pyplot as plt
X = np.arange(0,10,.5)

def Linear_function(X):
    """"
    Docstring: Linear_function(X)
    
    X: a Numpy array
    """
    m=4
    b=3
    Y=m*X+b
    plt.scatter(X,Y)
Linear_function(X)
