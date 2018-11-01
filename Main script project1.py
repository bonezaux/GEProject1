#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 12:16:22 2018

@author: SarahMagid
"""
import numpy as np
import os

def MainScript():
    userinput = True
    
    while userinput:
        print("""
              1. Load data
              2. Filter data
              3. Display statistics
              4. Generate plots
              5. Quit 
              """)
        userinput = input("Choose a menu point by entering the number: ")
        dataset = False
        
        if userinput == "1":
            print("Entered no.1")
            filename = input("Write the name of the datafile: ")
            while dataset == False:
                cwd = os.getcwd
                datapath = os.path.join(cwd,filename)
                if os.path.isfile(datapath):
                    dataset = True
                    from dataLoad import dataLoad
                    data = dataLoad(filename)
                else:
                    print("Filename is not valid, check spelling and try again")
                    
        elif userinput == "2":
            #Checking if user remembered to load in data
            if dataset == False:
                print("You must load the data first")
            else:
                print ("do something")
        elif userinput == "3":
            #Checking if user remembered to load in data
            if dataset == False:
                print("You must load the data first")
            else:
                from dataStatistics import dataStatistics
                print(""" 
                      1. Mean Temperature
                      2. Mean Growth rate
                      3. Standard deviation of temperature
                      4. Standard deviation of Growth rate 
                      5. Number of rows in data
                      6. Mean Growth rate when Temperature is less than 20 degrees
                      7. Mean Growth rate when Temperature is greater than 50 degrees
                      """)
                Statistics = input("Choose the number of the statistic you want calculated: ")
                dataStatistics(data, "Statistics")
        elif userinput == "4":
            #Checking if user remembered to load in data
            if dataset == False:
                print("You must load the data first")
            else:
                from dataPlot import dataPlot
                dataPlot(#Remember to put in filtered data here) 
        
        elif userinput == "5":
            break
        
        else:
            print("You have entered an invalid input. Please press a number from 1 to 5")
    return

MainScript()
