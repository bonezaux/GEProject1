# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:16:25 2018

@author: Carl
"""
import numpy as np
import matplotlib.pyplot as plt
import random
def dataPlot(data):
    """
    
    """
    bacteria = []
     #Add rows where bacteria=i+1 to that bacteria's row matrix
    for i in range(4):
        bacteria.append( data[data[:,2] == i+1])
    
    #Make a bar chart with the number of the bacteria as x and amount of observations as y
    plt.bar(np.array(range(4))+1, [len(x) for x in bacteria])
    plt.show()
    
    #Sort the bacteria arrays by temperature
    bacteria = [x[x[:,0].argsort()] for x in bacteria]
    
    #Plot all bacteria arrays, growth to temperature
    for single in bacteria:
        plt.plot(single[:,0], single[:,1])
    #Set appropriate axes
    plt.axis([19,61,0,30])
    plt.show()
    
    return bacteria



dat = np.array([]).reshape(0,3)
for x in range(21):
    dat = np.vstack((dat, np.array([random.randint(20, 60), random.randint(5,15), random.randint(1,4)])))

dataPlot(dat)
