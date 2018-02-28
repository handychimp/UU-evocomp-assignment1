# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:16:56 2018

@author: Tom
"""
import numpy as np
from random import shuffle

#1. Initialise a population

pop1 = np.random.randint(2, size=(10,100))


#2. Define fitness functions

def fitness( x, trap = False , random_linked = False, k = 4, d = 1.0 ):
    fitness_value = 0 
    
    if trap:
        y=x.copy()

        if random_linked:
             shuffle(y)
        
        for j in range (0,int(len(y)/k)):
            if sum(y[j*k:(j*k)+k])==k:
                fitness_value += k
            else:
                fitness_value += ( k - d - ((k-d)/(k-1)) * sum(y[j*k:j*k+k]) )
            
        return fitness_value        
    
    else:
        return sum(x)
    




 


