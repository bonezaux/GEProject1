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
import filter

def MainScript():
    data = np.array([])
    filterData = { "Bacteria" : [], "Growth": None}
    filterActive = False
    bacteriaNames = np.array(["Salmonella enterica", "Bacillus cereus", "Listeria", "Brochothrix thermosphacta"])
    
    while True:
        print("""
1. Load data
2. Filter data
3. Display statistics
4. Generate plots
5. Quit 
              """)
        filter.printFilter(filterData, filterActive, bacteriaNames)
        userinput = input("Choose a menu point by entering the number: ")
        
        if userinput == "1":
            #Ask user to input filename
            filename = input("Write the name of the data file: ")
            cwd = os.getcwd()
            datapath = os.path.join(cwd,filename)
            #Check if file exists
            if os.path.isfile(datapath) == True:
                data = dataLoad(filename)
                if(len(data) == 0):
                    print("Invalid file! No data loaded.")
                else:
                    print("Your file: '%s' has been loaded" % (filename))
                
            else:
                print("Filename is not valid, check spelling and try again")
                    
        elif userinput == "2":
            filterTmp = filter.filterMenu(filterData, filterActive, bacteriaNames)
            filterData = filterTmp[0]
            filterActive = filterTmp[1]
            
        elif userinput == "3":
            #Checking if user remembered to load in data first
            if len(data) == 0:
                print("\n" + "You must first load data.")
            else:
                options = ["Mean Temperature", "Mean Growth rate",
                           "Standard deviation of temperature",
                           "Standard deviation of growth rate",
                           "Number of rows in data",
                           "Mean Growth rate when Temperature is less than 20 degrees",
                           "Mean Growth rate when Temperature is greater than 50 degrees"]
                
                for i,option in enumerate(options):
                    print(str(i+1) + ". " + option)
                Statistics = False
                while Statistics == False:
                    Statistics = input("Choose the number of the statistic you want calculated: ")
                    if (not Statistics.isdigit()) or int(Statistics) < 1 or int(Statistics) > 7:
                        Statistics = False
                        print("Write an integer between one and seven.")
                stats = dataStatistics(filter.filteredData(data, filterData, filterActive), Statistics)
                if(stats != None):
                    print(options[int(Statistics)-1] + " is " + str(round(stats,3)))
                    filter.printFilter(filterData, filterActive, bacteriaNames)
                    input("Press enter to continue ")
                
        elif userinput == "4":
            #Checking if user remembered to load in data first
            if len(data) == 0:
                print("\n" + "You must first load data.")
            else:
                dataPlot(filter.filteredData(data, filterData, filterActive))
                filter.printFilter(filterData, filterActive, bacteriaNames)
                input("Press enter to continue ")
        
        elif userinput == "5":
            #quit
            break
        else:
            print("You have entered an invalid input. Please enter a number from 1 to 5")
    return

MainScript()
