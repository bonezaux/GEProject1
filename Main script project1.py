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
    dataset = False
    
    while userinput:
        print("""
              1. Load data
              2. Filter data
              3. Display statistics
              4. Generate plots
              5. Quit 
              """)
        userinput = input("Choose a menu point by entering the number: ")
        
        if userinput == "1":
            #Ask user to input filename
            filename = input("Write the name of the datafile: ")
            #Check if file exists
            while dataset == False:
                cwd = os.getcwd()
                datapath = os.path.join(cwd,filename)
                if os.path.isfile(datapath) == True:
                    dataset = True
                    print("Your file: '%s' has been loaded" % (filename))
                    print(dataset)
                    data = filename
                else:
                    print("Filename is not valid, check spelling and try again")
                    
        elif userinput == "2":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
            else:
                print ("Choose a filter and print what filter is chosen ")
        elif userinput == "3":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
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
                dataStatistics(data, Statistics)
        elif userinput == "4":
            #Checking if user remembered to load in data first
            if dataset == False:
                print("\n" + "You must start by loading the data.")
            else:
                from dataPlot import dataPlot
                dataPlot()#Remember to put in filtered data here
        
        elif userinput == "5":
            #quit
            break
        else:
            print("You have entered an invalid input. Please press a number from 1 to 5")
    return

MainScript()

