# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:04:40 2018

@author: William
"""

import pandas as pd
import numpy as np

def dataLoad(filename):
    """Loads a file of data, prints error message when values are
    out of bound, and removes the inconsistent lines.
    
    Input: A space-separated data file with 3 numeric-valued columns:
        temperature, growth rate, and bacteria - in this order.
    
    Output: An N x 3 matrix, where N denotes the valid rows. Valid
        rows have (10 <= temperature <= 60), (Growth rate >= 0), 
        (Bacteria in [1,2,3,4]).
            String(s) specifying invalid rows.
    """
    # Import the file and convert it to numpy array
    data = pd.read_csv(filename,delim_whitespace=True)
    data = np.array(data)
    
    # The 3 fields [columns] of the data
    temp = data[:,0]
    growth = data[:,1]
    bacteria = data[:,2]
    
    # Tuples of lines with deviations ((index of error) + 1). Made into tuples for aesthetics.
    temp_dev = tuple(np.where(np.logical_or(temp > 60, temp < 10))[0]+1)
    growth_dev = tuple(np.where(growth < 0)[0]+1)
    bacteria_dev = tuple(np.where(np.isin(bacteria, [1,2,3,4]) == False)[0]+1)
    
    # Print error if there is one or more and omit line if there is not
    empty = ()
    if temp_dev != empty:
        print("Lines %s were removed because their temperature was either below 10 or above 60." % (temp_dev,))
    if growth_dev != empty:
        print("Lines %s were removed because the growth rate was negative" % (growth_dev,))
    if bacteria_dev != empty:
        print("Lines %s were removed because only values 1, 2, 3, or 4 are valid to denote the bacteria." % (bacteria_dev,))
    
    # Update data
    invalid = tuple(set(temp_dev+growth_dev+bacteria_dev))
    print()
    print()
    data = np.delete(data,np.asarray(invalid)-1,0)
    return data

data = dataLoad('test_2.txt')

print(data)