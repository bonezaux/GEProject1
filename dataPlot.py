# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:16:25 2018

@author: Carl
"""
import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    """
    Given an Nx3 bacteria data matrix matrix,
    plots a bar chart with the number of rows for each bacteria type in the Nx3 matrix
    and a graph for the growth rate of each bacteria type by temperature on the same coordinate system
    """
    if(data.size == 0):
        print("No data selected. Change filter or load new file.")
        return
    bacteriaNames = ['Salmonella\nenterica', 'Bacillus\ncereus', 'Listeria', 'Brochothrix\nthermosphacta']
    
    bacteria = []
    #Split data matrix into four matrices, one for each bacteria type.
    for i in range(4):
        bacteria.append( data[data[:,2] == i+1])
    
    bacteriaAmounts = [len(x) for x in bacteria]
    
    #Make a bar chart with the number of the bacteria as x and amount of observations as y
    plt.bar(np.array(range(4)), bacteriaAmounts)
    #Set appropriate axes & legend
    plt.ylabel('Measurements')
    plt.xlabel('Bacteria type')
    plt.title('Number of bacteria measurements')
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
    plt.title('Growth rate by temperature')
    #Make a legend for the bacteria growth plots for all bacterias we have measurements of
    legend = [(plts[x][0], bacteriaNames[x]) for x in range(4) if bacteriaAmounts[x] > 0]
    plt.legend((x[0] for x in legend), (x[1] for x in legend))
    plt.show()
