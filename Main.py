# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 00:41:59 2018

@author: Tom
"""
#import os
#os.chdir('C:/Users/Tom/Documents/UU/Evolutionary Computing/UU-evocomp-assignment1')

from __future__ import print_function
import Genetic_Algorithm as ga
import numpy as np
import sys
from multiprocessing import Pool
from functools import partial
import multiprocessing as mp
import pickle


if sys.version_info[:2] < (3, 3):
    old_print = print
    def print(*args, **kwargs):
        flush = kwargs.pop('flush', False)
        old_print(*args, **kwargs)
        if flush:
            file = kwargs.get('file', sys.stdout)
            # Why might file=None? IDK, but it works for print(i, file=None)
            file.flush() if file is not None else sys.stdout.flush()

#Minimum Population Functions
def Minimum_Population_UX(**kwargs):
    UX_success_counter = 0
    pop_size = 10
    UX_results = []
    while UX_success_counter < 24 and pop_size <= 1280:
        print(pop_size,flush=True)
        Trial_results = []
        UX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_UX(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                UX_success_counter += 1        
            print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]),flush=True)
    
        UX_results.append((pop_size,Trial_results))
        if UX_success_counter < 24:
            pop_size = pop_size * 2
    
    UX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size,flush=True)
        Trial_results = []
        UX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_UX(pop_size,100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                UX_success_counter += 1
                print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]),flush=True)
        
        UX_results.append((pop_size,Trial_results))    
        if UX_success_counter >= 24:
            a = pop_size
            pop_size = int((a+b)/2)
        else:
            b = pop_size
            pop_size = int((a+b)/2)
    return UX_results

def Seeded_Experiment(seed,**kwargs):
    return partial(ga.Experiment_UX,pop_size,string_length=100,**kwargs)

def Minimum_Population_UX_Parallel(**kwargs):
    UX_success_counter = 0
    pop_size = 10
    UX_results = []
    while UX_success_counter < 24 and pop_size <= 10:
        print(pop_size,flush=True)
        Trial_results = []
        UX_success_counter = 0
        map_func = partial(ga.Experiment_UX,pop_size=pop_size,string_length=100,**kwargs)
        p=Pool()
        Trial_results=p.map(map_func,range(0,25))
        p.close()
        p.join()
  
        UX_results.append((pop_size,Trial_results))
        
        for i in range (0,len(Trial_results)):
            if int(Trial_results[i][len(Trial_results[i])-1][2])==100:
                UX_success_counter += 1
        print('Successes: ' + str(UX_success_counter) + ' out of 25')
        
        if UX_success_counter < 24:
            pop_size = pop_size * 2
    
    UX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size,flush=True)
        Trial_results = []
        UX_success_counter = 0
        map_func = partial(ga.Experiment_UX,pop_size=pop_size,string_length=100,**kwargs)
        p=Pool()
        Trial_results=p.map(map_func,range(0,25))
        p.close()
        p.join()
        UX_results.append((pop_size,Trial_results))
        
        for i in range (0,len(Trial_results)):
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                UX_success_counter += 1
        print('Successes: ' + str(UX_success_counter) + ' out of 25')
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
        print(pop_size,flush=True)
        Trial_results = []
        TWOX_success_counter = 0
        for i in range(0,25):
            Trial_results.append(ga.Experiment_2X(pop_size=pop_size,string_length=100,**kwargs))
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1        
            print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]),flush=True)
    
        TWOX_results.append((pop_size,Trial_results))
        if TWOX_success_counter < 24:
            pop_size = pop_size * 2
    
    TWOX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size,flush=True)
        Trial_results = []
        TWOX_success_counter = 0
        for i in range(0,25):
            Trial_results=ga.Experiment_2X(pop_size,100,**kwargs)
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1
                print('Trial ' + str(i) + ' gives fitness: ' + str(Trial_results[i][len(Trial_results[i])-1][2]),flush=True)
        
        TWOX_results.append((pop_size,Trial_results))    
        if TWOX_success_counter >= 24:
            a = pop_size
            pop_size = int((a+b)/2)
        else:
            b = pop_size
            pop_size = int((a+b)/2)
    return TWOX_results

def test_fun(**kwargs):
    pop_size = 10
    map_func = partial(ga.Experiment_2X,pop_size=pop_size,string_length=100,**kwargs)
    return map_func

test = test_fun(trap=True)
test.keywords
test.args

def Minimum_Population_2X_Parallel(**kwargs):
    TWOX_success_counter = 0
    pop_size = 10
    TWOX_results = []
    #seeds = np.random.randint(10000,size=(25))
    while TWOX_success_counter < 24 and pop_size <= 10:
        print(pop_size,flush=True)
        Trial_results = []
        TWOX_success_counter = 0
        pop_size = 10
        map_func = partial(ga.Experiment_2X,pop_size=pop_size,string_length=100,**kwargs)
        p=Pool()
        Trial_results=p.map(map_func,range(0,25))
        p.close()
        p.join()
  
        TWOX_results.append((pop_size,Trial_results))
        
        for i in range (0,len(Trial_results)):
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1
        print('Successes: ' + str(TWOX_success_counter) + ' out of 25')
        
        if TWOX_success_counter < 24:
            pop_size = pop_size * 2
    
    TWOX_success_counter = 0
    a = pop_size
    b = int(pop_size/2)
    pop_size = int((a+b)/2)
    while a-b >= 10:
        print(pop_size,flush=True)
        Trial_results = []
        TWOX_success_counter = 0
        p=Pool()
        Trial_results=p.map(map_func,range(0,25))
        p.close()
        p.join()
        TWOX_results.append((pop_size,Trial_results))
        
        for i in range (0,len(Trial_results)):
            if Trial_results[i][len(Trial_results[i])-1][2]==100:
                TWOX_success_counter += 1
        print('Successes: ' + str(TWOX_success_counter) + ' out of 25')  
        if TWOX_success_counter >= 24:
            a = pop_size
            pop_size = int((a+b)/2)
        else:
            b = pop_size
            pop_size = int((a+b)/2)
    return TWOX_results


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
    Results_Random_Deceptive_Trap_UX = Minimum_Population_UX_Parallel(trap=True,random_linked=True)
    with open('Random_Deceptive_UX','wb') as fp:
        pickle.dump(Results_Random_Deceptive_Trap_UX,fp)
    
    Results_Random_Deceptive_Trap_2X = Minimum_Population_2X_Parallel(trap=True,random_linked=True)
    with open('Random_Deceptive_2X','wb') as fp:
        pickle.dump(Results_Random_Deceptive_Trap_2X,fp)   
    
    Results_Random_NonDeceptive_Trap_UX = Minimum_Population_UX_Parallel(trap=True,random_linked=True,d=2.5)
    with open('Random_NonDeceptive_UX','wb') as fp:
        pickle.dump(Results_Random_NonDeceptive_Trap_UX,fp) 
        
    Results_Random_NonDeceptive_Trap_2X = Minimum_Population_2X_Parallel(trap=True,random_linked=True,d=2.5)
    with open('Random_NonDeceptive_2X','wb') as fp:
        pickle.dump(Results_Random_NonDeceptive_Trap_2X,fp) 
        
  
    
    #Results_Random_Deceptive_Trap_2X = Minimum_Population_2X(trap=True,random_linked=True)
    #Results_Random_NonDeceptive_Trap_UX = Minimum_Population_UX(trap=True,random_linked=True,d=2.5)
    #Results_Random_NonDeceptive_Trap_2X = Minimum_Population_UX(trap=True,random_linked=True,d=2.5)

    #Results_CountOnes_UX = Minimum_Population_UX()
    #Results_CountOnes_2X = Minimum_Population_2X()
    #Results_DecepTrap_UX = Minimum_Population_UX(trap=True)
    #Results_DecepTrap_2X = Minimum_Population_2X(trap=True)
    #Results_NonDecepTrap_UX = Minimum_Population_UX(trap=True,d=2.5)
    #Results_NonDecepTrap_2X = Minimum_Population_2X(trap=True,d=2.5)


#os.getpid()


                