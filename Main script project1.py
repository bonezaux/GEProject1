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


def filteredData(data, filterData, filterActive):
    """
    Filters data according to active filters without changing the data array.
    """
    if not filterActive:
        return data
    result = data
    if(len(filterData["Bacteria"]) > 0):
        result = result[result[:,2]==(filterData["Bacteria"][0]+1)]
    if(filterData["Growthmin"] != None and (filterData["Growthmax"]) != None):
        result = result[result[:,1] <= filterData["Growthmax"] and result[:,1] >= filterData["Growthmin"]]
    return result

def MainScript():
    userinput = True
    dataset = False
    filterData = { "Bacteria" : [], "Growthmin" : None, "Growthmax" : None}
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
            if(filterData["Growthmin"] != None and filterData["Growthmax"] != None):
                print(str(filterData["Growthmin"]) + " <= Growth rate <= " + str(filterData["Growthmax"]))
        userinput = input("Choose a menu point by entering the number: ")
        
        if userinput == "1":
            #Unset data
            dataset = False
            
        		#Ask user to input filename
            filename = input("Write the name of the datafile: ")
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
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
            else:
                print("""Filter menu
               1. Bacteria type
               2. Growth rate range
               3. Dis- or enable filter""")
                fnum = input("Choose a menu point: ")
                if(fnum.isdigit()):
                    if(int(fnum) == 1):
                        #Print bacteria names
                        print("\n".join([str(x+1)+". "+bacteriaNames[x] for x in range(4)]))
                        
                        #Get a bacteria number
                        bacteria = input("Pick a bacteria number to filter by: ")
                        
                        #Ensure that a number between 1 and 4 is provided
                        if not bacteria.isdigit() or int(bacteria) < 1 or int(bacteria) > 4:
                            print("You need to write a number between 1 and 4.")
                        else:
                            #Subtracting one to match array indices
                            bacteria = int(bacteria)-1
                            print("Filtering by " + bacteriaNames[bacteria])
                            filterData["Bacteria"] = [bacteria]
                            filterActive=True
                        
                    elif(int(fnum) == 2):
                        minimum = None
                        maximum = None
                        
                        minimum = input("Insert a number for the minimum growth rate: ")
                        if (not minimum.isdigit()) or float(minimum) < 0 or int(minimum) > 1:
                            print("You need to write a number between 0 and 1.")
                        else:
                            maximum = input("Insert a number for the maximum growth rate: ")
                            if (not maximum.isdigit()) or int(maximum) < 0 or int(maximum) > 1:
                                print("You need to write a number between 0 and 1.")
                        
                        #Checking if the minimum is less than maximum
                        if minimum != None and maximum !=None:
                            if not int(minimum) <= int(maximum):
                                print("Invalid range. Minimum larger than or equal to maximum.")
                            else:
                                filterData["Growthmin"] = minimum
                                filterData["Growthmax"] = maximum
                                filterActive=True
                            
                    elif(int(fnum) == 3):
                        print(""" 
                              1. Add a bacteriatype
                              2. Reset bacteriafiltering
                              3. Reset growth rate filter
                              4. Reset all filters
                              """)
                        fchange = input("Choose a menupoint")
                        if fchange =="1":
                            #Print the bacteria names that are possible to choose
                            print("\n".join([str(x+1)+". "+bacteriaNames[x] for x in range(4) if not x in filterData["Bacteria"]]))
                            #Get a bacteria number
                            bacteria = input("Pick a bacteria number to filter by: ")
                        
                            #Ensure that a valid number between 1 and 4 is provided
                            if not bacteria.isdigit() or int(bacteria) < 1 or int(bacteria) > 4 or int(bacteria-1) in filterData["Bacteria"]:
                                print("You need to write a valid bacteria number.")
                            else:
                            #Subtracting one to match array indices
                                bacteria = int(bacteria)-1
                                print("Filtering by " + bacteriaNames[bacteria])
                                filterData["Bacteria"] += [bacteria]
                                filterActive=True
    
                        elif fchange == "2":
                            #Removes bacteriafiltering
                            filterData["Bacteria"] = []
                            print("Bacterierefiltering have been reset")
                            
                            #If no growthratefilter,there are no active filters
                            if filterData["Growthmin"]==None and filterData["Growthmax"]==None:
                                filterActive=False
                            
                        elif fchange == "3":
                            #Removes growth range filtering
                            filterData["Growthmin"] = None
                            filterData["Growthmax"] = None
                            print("Growth rate filter have been reset")
                           
                            #If no bacteriafilter, there are no active filters
                            if filterData["Bacteria"]==[]:
                                filterActive=False
                                
                        elif fchange == "4":
                            #Reset all filters
                            filterData["Growthmin"] = None
                            filterData["Growthmax"] = None
                            filterData["Bacteria"] = []
                            #No active filters
                            filterActive=False
                            print("All filters have been reset")
                            
                        else:
                            print("You should have chosen a menupoint between 1 and 4")
                    else:
                        print("That is not a valid filter.")
                else:
                    print("Write a number!")
        elif userinput == "3":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
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
            
            print(options[int(Statistics)-1] + " is " + str(dataStatistics(filteredData(data, filterData, filterActive), Statistics)))
        elif userinput == "4":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
            else:
                dataPlot(filteredData(data, filterData, filterActive))
        
        elif userinput == "5":
            #quit
            break
        else:
            print("You have entered an invalid input. Please press a number from 1 to 5")
    return

MainScript()
