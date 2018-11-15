# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:18:54 2018

@author: carl
"""
import numpy as np

def isFloat(string):
    """
    Checks whether a string is a float. Returns either true or false.
    """
    try:
        float(string)
    except ValueError:
        return False;
    return True;

def filteredData(data, filterData, filterActive):
    """
    Filters data according to active filters without changing the data array.
    """
    if not filterActive:
        return data
    result = data
    
    if(len(filterData["Bacteria"]) > 0):
        #Remove all data and add filtered bacteria back in one at a time
        result = np.array([[0,0,0]])
        for bac in filterData["Bacteria"]:
            result = np.concatenate((result, data[data[:,2]==(bac+1)]), axis=0)
        result = result[1:,:]
        
    if(filterData["Growth"] != None):
        #select only rows with growth rate btwn max and min
        result = result[result[:,1] <= filterData["Growth"][1]]
        result = result[result[:,1] >= filterData["Growth"][0]]
    
    return result

def printFilter(filterData, filterActive, bacteriaNames):
    """
    Prints current filter, if any, based on given filter data. Needs the bacteria names to print correctly.
    """
    if filterActive:
            print("Current filter:")
            if(len(filterData["Bacteria"]) > 0):
                print("Bacteria: " + (", ".join(bacteriaNames[filterData["Bacteria"]])))
            if(filterData["Growth"] != None):
                print(str(filterData["Growth"][0]) + " <= Growth rate <= " + str(filterData["Growth"][1]))

def filterMenu(filterData, filterActive, bacteriaNames):
    """
    Takes the user through the menu for changing the filter.
    Returns a tuple with the new filterData and filterActive.
    """
    print(""" Filter menu
1. Set or add bacteria type to filter
2. Set growth rate range filter
3. Remove bacteria filter
4. Remove growth rate filter
5. Remove all filters""")
    fnum = input("Choose a menu point: ")
    
    if(not fnum.isdigit()):
        print("Write a number!")
        return (filterData, filterActive)
    
    #Add/set bacteria filter
    if fnum == "1":
        #Print the bacteria names that are possible to choose
        print("\n".join([str(x+1)+". "+bacteriaNames[x] for x in range(4) if not x in filterData["Bacteria"]]))
        #Get a bacteria number
        bacteria = input("Pick a bacteria number to filter by: ")
    
        #Ensure that a valid number between 1 and 4 is provided
        if not bacteria.isdigit() or int(bacteria) < 1 or int(bacteria) > 4 or int(bacteria)-1 in filterData["Bacteria"]:
            print("You need to write a valid bacteria number.")
        else:
            #Subtracting one to match array indices
            bacteria = int(bacteria)-1
            print("Filtering by " + bacteriaNames[bacteria])
            filterData["Bacteria"] += [bacteria]
            filterActive=True
    
    #Set growth rate filter
    elif fnum == "2":
        minimum = None
        maximum = None
        minimum = input("Insert a number for the minimum growth rate: ")
        if (not isFloat(minimum)) or float(minimum) < 0 or float(minimum) > 1:
            print("You need to write a number between 0 and 1.")
        else:
            maximum = input("Insert a number for the maximum growth rate: ")
            if (not isFloat(maximum)) or float(maximum) < 0 or float(maximum) > 1:
                print("You need to write a number between 0 and 1.")
        
        #Checking if the minimum is less than maximum
        if minimum != None and maximum !=None:
            if not float(minimum) <= float(maximum):
                print("Invalid range. Minimum larger than or equal to maximum.")
            else:
                filterData["Growth"] = (float(minimum), float(maximum))
                filterActive=True
    
    #Remove bacteria filter        
    elif fnum == "3":
        filterData["Bacteria"] = []
        print("Bacteria filter has been removed")
        
        #If no growth rate filter,there are no active filters
        if filterData["Growth"]==None:
            filterActive=False

    #Remove growth range filter            
    elif fnum == "4":
        filterData["Growth"] = None
        print("Growth rate filter have been removed")
       
        #If no bacteria filter, there are no active filters
        if filterData["Bacteria"]==[]:
            filterActive=False
    
    #Remove all filters    
    elif fnum == "5":
        filterData["Growth"] = None
        filterData["Bacteria"] = []
        #No active filters
        filterActive=False
        print("All filters have been reset")
    
    else:
        print("That is not a valid menu point.")
    
    return (filterData, filterActive)
