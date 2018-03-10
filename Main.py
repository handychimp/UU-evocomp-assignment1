# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 00:41:59 2018

@author: Tom
"""
#import os
#os.chdir('C:/Users/Tom/Documents/UU/Evolutionary Computing/UU-evocomp-assignment1')

import Genetic_Algorithm as ga
import numpy as np
from collections import namedtuple
import matplotlib as mp

#Minimum Population Functions
def Minimum_Population_UX(**kwargs):
    UX_success_counter = 0
    pop_size = 10
    UX_results = []
    while UX_success_counter < 24 and pop_size <= 1280:
        print(pop_size)
        Trial_results = []
        UX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_UX(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                UX_success_counter += 1        
            print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]))
    
        UX_results.append((pop_size,Trial_results))
        if UX_success_counter < 24:
            pop_size = pop_size * 2
    
    UX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size)
        Trial_results = []
        UX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_UX(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                UX_success_counter += 1
                print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]))
        
        UX_results.append((pop_size,Trial_results))    
        if UX_success_counter >= 24:
            a = pop_size
            pop_size = int((a+b)/2)
        else:
            b = pop_size
            pop_size = int((a+b)/2)
    return UX_results

#a Uniform Crossover
def Minimum_Population_2X(**kwargs):
    TWOX_success_counter = 0
    pop_size = 10
    TWOX_results = []
    while TWOX_success_counter < 24 and pop_size <= 1280:
        print(pop_size)
        Trial_results = []
        TWOX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_2X(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1        
            print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]))
    
        TWOX_results.append((pop_size,Trial_results))
        if TWOX_success_counter < 24:
            pop_size = pop_size * 2
    
    TWOX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size)
        Trial_results = []
        TWOX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_2X(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1
                print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]))
        
        TWOX_results.append((pop_size,Trial_results))    
        if TWOX_success_counter >= 24:
            a = pop_size
            pop_size = int((a+b)/2)
        else:
            b = pop_size
            pop_size = int((a+b)/2)
    return TWOX_results

from multiprocessing import Pool

def Random_Linking_Funcs(x):
    if x == 1:    
        results = Minimum_Population_UX(trap=True,random_linked=True)
    elif x==2:
        results = Minimum_Population_2X(trap=True,random_linked=True)
    elif x == 3:
        results = Minimum_Population_UX(trap=True,random_linked=True,d=2.5)
    elif x == 4:
        results = Minimum_Population_UX(trap=True,random_linked=True,d=2.5)

    return results    
    

if __name__ == '__main__':
    __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
    array = [1,2,3,4]
    p = Pool()
    result= p.map(Random_Linking_Funcs,array)
    p.close()
    p.join()


#Results_CountOnes_UX = Minimum_Population_UX()
#Results_CountOnes_2X = Minimum_Population_2X()
#Results_DecepTrap_UX = Minimum_Population_UX(trap=True)
#Results_DecepTrap_2X = Minimum_Population_2X(trap=True)
#Results_NonDecepTrap_UX = Minimum_Population_UX(trap=True,d=2.5)
#Results_NonDecepTrap_2X = Minimum_Population_2X(trap=True,d=2.5)




