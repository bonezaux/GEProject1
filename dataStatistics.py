#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:03:18 2018

@author: SarahMagid
"""

import numpy as np
def dataStatistics(data, statistics):
    """ This function computes one of several statistics based on the data.
    The function takes two inputs. An Nx3 matrix of data with the columns 
    temperature, growth rate and bacteria. And a string specifying the the 
    statistics that should be calculated."""
    
    if statistics == "1":
        result = np.mean(data[:,0]) 
    elif statistics == "2":
        result = np.mean(data[:,1])
    elif statistics == "3":
        #To calculate the variance I take each difference to mean temperature,
        #square it, and then average the result.
        #Standart deviation is the square root of variance
        result = np.std(data[:,0])
    elif statistics == "4":
        #variance = sum(abs(data[:,1]-np.mean(data[:,1]))**2)/len(data)
        #result = np.sqrt(variance)
        result = np.std(data[:,1])
    elif statistics == "5":
        #Python has a built in shape function, that outputs number of rows and columns in an array.
        #But when rows = 1, the function only outputs number of columns.
        #Thus I make shure, that if number of rows = 1, the output is 1.
        if data.shape == 1:
            result = 1
        else:
            result = data.shape[0]
    elif statistics == "6":
        #temp array with the temperatures only
        temp = data[:,0]
        #New matrix is found without the rows, where temp > 20 degrees
        new = data[temp < 20]
        #The mean growth rate is calculated:
        result = np.mean(new[:,1])
    elif statistics == "7":
        temp = data[:,0]
        #New matrix is found without the rows, where temp > 50 degrees
        new = data[temp > 50]
        result = np.mean(new[:,1])
    else:
        print("Something went wrong with your input. Check if it is number between 1 and 7")
    return result

from dataload import dataLoad
datafile = dataLoad('test.txt')

dataStatistics(datafile,"1")