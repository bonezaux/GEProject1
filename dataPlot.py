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
    bacteriaNames = ['Salmonella\nenterica', 'Bacillus\ncereus', 'Listeria', 'Brochothrix\nthermosphacta']
    
    bacteria = []
     #Add rows where bacteria=i+1 to that bacteria's row matrix
    for i in range(4):
        bacteria.append( data[data[:,2] == i+1])
    
    bacteriaAmounts = [len(x) for x in bacteria]
    
    #Make a bar chart with the number of the bacteria as x and amount of observations as y
    plt.bar(np.array(range(4)), bacteriaAmounts)
    #Set appropriate axes & legend
    plt.ylabel('Bacteria')
    plt.xlabel('Type')
    plt.title('Number of bacteria types')
    #Write names and amounts of bacteria types on x-axis
    plt.xticks(range(0,4), [str(x[1]) + " " + x[0] for x in zip(bacteriaNames,bacteriaAmounts)])
    #Make single ticks all the way to the most measured bacteria
    plt.yticks(np.arange(0,max(bacteriaAmounts)+1, int(max(bacteriaAmounts)/5)))
    plt.show()
    
    #Sort the bacteria arrays by temperature
    bacteria = [x[x[:,0].argsort()] for x in bacteria]
    
    maxGrowth = max(data[:,1])
    
    plts = []
    #Plot all bacteria arrays, growth to temperature
    for single in bacteria:
        plts.append(plt.plot(single[:,0], single[:,1]))
    #Set appropriate axes & legend
    plt.axis([10,60,0,maxGrowth+0.1])
    plt.ylabel('Growth rate')
    plt.yticks(np.arange(0, maxGrowth+0.1, maxGrowth/8))
    plt.xlabel('Temperature')
    #Make a legend for the bacteria growth plots for all bacterias we have measurements of
    plt.legend((plts[x][0] for x in range(4) if bacteriaAmounts[x] > 0), bacteriaNames)
    plt.show()
    
    return bacteria



dat = np.array([]).reshape(0,3)
for x in range(61):
    dat = np.vstack((dat, np.array([x, x**2/(61**2), random.randint(1,4)])))

dataPlot(dat)
