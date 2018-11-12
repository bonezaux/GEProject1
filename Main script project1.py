#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:16:22 2018

@author: SarahMagid
"""

import numpy as np
import os
from dataload import dataLoad
from dataStatistics import dataStatistics
from dataPlot import dataPlot

#Apparently how you check whether something is a float in python.
def isFloat(string):
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

def MainScript():
    userinput = True
    dataset = False
    filterData = { "Bacteria" : [], "Growth": None}
    filterActive = False
    bacteriaNames = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    
    while userinput:
        print("""
              1. Load data
              2. Filter data
              3. Display statistics
              4. Generate plots
              5. Quit 
              """)
        if filterActive:
            print("Current filter:")
            if(len(filterData["Bacteria"]) > 0):
                print("Bacteria: " + (", ".join(bacteriaNames[filterData["Bacteria"]])))
            if(filterData["Growth"] != None):
                print(str(filterData["Growth"][0]) + " <= Growth rate <= " + str(filterData["Growth"][1]))
        userinput = input("Choose a menu point by entering the number: ")
        
        if userinput == "1":
            #Unset data
            dataset = False
            
        		#Ask user to input filename
            filename = input("Write the name of the data file: ")
            cwd = os.getcwd()
            datapath = os.path.join(cwd,filename)
            #Check if file exists
            if os.path.isfile(datapath) == True:
                dataset = True
                print("Your file: '%s' has been loaded" % (filename))
                data = dataLoad(filename)
            else:
                print("Filename is not valid, check spelling and try again")
                    
        elif userinput == "2":
            print(""" Filter menu
           1. Set or add bacteria type to filter
           2. Set growth rate range filter
           3. Remove bacteria filter
           4. Remove growth rate filter
           5. Remove all filters""")
            fnum = input("Choose a menu point: ")
            if(not fnum.isdigit()):
                print("Write a number!")
                continue
            
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
                        
            elif fnum == "3":
                #Removes bacteria filter
                filterData["Bacteria"] = []
                print("Bacteria filter has been removed")
                
                #If no growth rate filter,there are no active filters
                if filterData["Growth"]==None:
                    filterActive=False
                    
            elif fnum == "4":
                #Removes growth range filter
                filterData["Growth"] = None
                print("Growth rate filter have been removed")
               
                #If no bacteria filter, there are no active filters
                if filterData["Bacteria"]==[]:
                    filterActive=False
                    
            elif fnum == "5":
                #Remove all filters
                filterData["Growth"] = None
                filterData["Bacteria"] = []
                #No active filters
                filterActive=False
                print("All filters have been reset")
            
            else:
                print("That is not a valid menu point.")
                    
        elif userinput == "3":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must first load data.")
            else:
                options = ["Mean Temperature", "Mean Growth rate",
                           "Standard deviation of temperature",
                           "Standard deviation of growth rate",
                           "Number of rows in data",
                           "Mean Growth rate when Temperature is less than 20 degrees",
                           "Mean Growth rate when Temperature is greater than 50 degrees"]
                print(""" 
          1. Mean Temperature
          2. Mean Growth rate
          3. Standard deviation of temperature
          4. Standard deviation of Growth rate 
          5. Number of rows in data
          6. Mean Growth rate when Temperature is less than 20 degrees
          7. Mean Growth rate when Temperature is greater than 50 degrees
                      """)
                Statistics = False
                while Statistics == False:
                    Statistics = input("Choose the number of the statistic you want calculated: ")
                    if (not Statistics.isdigit()) or int(Statistics) < 1 or int(Statistics) > 7:
                        Statistics = False
                        print("Write an integer between one and seven.")
                stats = dataStatistics(filteredData(data, filterData, filterActive), Statistics)
                if(stats != None):
                    print(options[int(Statistics)-1] + " is " + str(round(stats,3)))
                
        elif userinput == "4":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must first load data.")
            else:
                dataPlot(filteredData(data, filterData, filterActive))
        
        elif userinput == "5":
            #quit
            break
        else:
            print("You have entered an invalid input. Please enter a number from 1 to 5")
    return

MainScript()
