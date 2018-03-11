# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 15:16:56 2018

@author: Tom
"""
import numpy as np
import random
from operator import itemgetter
import os
import multiprocessing as mp
import time

#1. Define fitness functions
def fitness( x, trap = False , random_linked = False, k = 4, d = 1.0 ):
    fitness_value = 0 
    
    if trap:
        y=x.copy()

        if random_linked:
             random.shuffle(y)
        
        for j in range (0,int(len(y)/k)):
            if sum(y[j*k:(j*k)+k])==k:
                fitness_value += k
            else:
                fitness_value += ( k - d - ((k-d)/(k-1)) * sum(y[j*k:j*k+k]) )
            
        return fitness_value        
    
    else:
        return sum(x)

#2. Define crossover functions   
def crossover( p1, p2, cross_points = 1):
    #Cannot cross after last point in string
    #All points at least one bit apart
    #crossover points in this algorthm taken as up to the index
    cross_locations = sorted(random.sample(range(1,len(p1)), cross_points))
    #add the end of string as final cross point
    cross_locations += [len(p1)]
      
    #boolean to store which parent we're buildign from for multi-crossover
    first_parent = True
    last_crossover=0
    c1=[]
    c2=[]
    
    for cross_point in cross_locations:
        
        if first_parent:     
            c1 += p1[last_crossover:cross_point]
            c2 += p2[last_crossover:cross_point]
        else:
            c1 += p2[last_crossover:cross_point]
            c2 += p1[last_crossover:cross_point]
        first_parent = not first_parent
        last_crossover = cross_point
        
    return [c1,c2]

#3. Define selection method
#Take in a tuple of the member and its fitness score, return the best 2
def family_competition(parents,children,continue_algorithm):      
    #combine family, children first so sort prioritises.
    #sort by descending fitness and take the first 2.
    selection_error = 0
    family = children + parents
    family.sort(key=itemgetter(1),reverse=True)
    
    for member in children:
        if member in family[0:2]:
            continue_algorithm=True
    
    selection_check1 = set([i for i, x in enumerate(family[0]) if x == 0])
    selection_check2 = [i for i, x in enumerate(family[0]) if x == 0 and i in selection_check1]        
    
    for i in selection_check2:
        if parents[0][i] == 1 or parents[1][i] == 1:
            selection_error=selection_error+1
    
    return (family[0:2],selection_error)

#4. Apply functions across a population
#a. Fitness
def pop_fitness(pop,fitness_function,**kwargs):
    pop_fitness = []
    for row in pop:
        pop_fitness.append((list(row),fitness_function(row,**kwargs)))
    return pop_fitness

#b. Crossover
def create_children(pop,crossover_function,**kwargs):
    child_pop=[]
    for i in range(0,int(len(pop)/2)):
        children = crossover_function(list(pop[2*i][0]),list(pop[2*i + 1][0]),**kwargs)
        child_pop.append(children[0])
        child_pop.append(children[1])
        
    return np.asarray(child_pop)

#c. Selection
#take in tuples of the member and its fitness
def selection(parent_pop,child_pop,continue_algorithm,selection_function):
    new_pop=[]
    selection_errors=0
    continue_algorithm = False
    for i in range(0,int(len(parent_pop)/2)):
        selected = selection_function(parent_pop[2*i:2*i + 2],child_pop[2*i:2*i + 2],continue_algorithm)
        new_pop.append(selected[0][0])
        new_pop.append(selected[0][1])
        selection_errors += selected[1]
    
    return (new_pop,selection_errors)

def Experiment_UX(seed,pop_size,string_length=100,epochs=1000,**kwargs):
    #Generate Population and Initialise vars
    print('Experiment_UX started...' + str(seed),flush=True)
    start=time.time()
    local_state = np.random.mtrand.RandomState(seed)
    pop = local_state.randint(2,size=(pop_size,string_length))
    pop_log = []
    continue_algorithm = True
    identical_gen_count = 0
    generation = 0
    selection_errors = 0
    
    #Loop while children are selected
    while continue_algorithm == True and generation < epochs + 1:
        #Shuffle for all but 0th gen
        if generation != 0:
            np.random.shuffle(pop)
        else:
            #Fill in fitness for 0th gen as not calculated
            pop = pop_fitness(pop,fitness,**kwargs)
     
        child_pop = create_children(pop,crossover)
        child_pop = pop_fitness(child_pop,fitness,**kwargs)
    
        #Continue_algorithm flag is evaluated again within this function
        next_pop = selection(pop,child_pop,continue_algorithm,family_competition)
        #Log some stats on the algorithm        
        total_bits = sum(j for i,j in pop)        
        pop_log.append((generation,total_bits, total_bits/len(pop),selection_errors))        


        if np.array_equal(pop,next_pop[0]):
            identical_gen_count += 1
            if identical_gen_count >= 5:
                continue_algorithm=False
        else:    
            pop = next_pop[0]
            selection_errors = next_pop[1]
            generation +=1
            identical_gen_count = 0
    end = time.time() 

    print('Experiment_UX finished...Trial fitness:' + str(pop_log[len(pop_log)-1][2]),flush=True)
    #pop_log.append((end-start))
    return (pop_log,(end-start))
        


def Experiment_2X(seed,pop_size,string_length=100,epochs=1000,**kwargs):
    #Generate Population and Initialise vars
    print('Experiment_2X started...' + str(seed),flush=True)
    start=time.time()
    local_state = np.random.mtrand.RandomState(seed)
    pop = local_state.randint(2,size=(pop_size,string_length))
    pop_log = []
    continue_algorithm = True
    identical_gen_count = 0
    generation = 0
    selection_errors = 0
    
    #Loop while children are selected
    while continue_algorithm == True and generation < epochs + 1:
        #Shuffle for all but 0th gen
        if generation != 0:
            np.random.shuffle(pop)
        else:
            #Fill in fitness for 0th gen as not calculated
            pop = pop_fitness(pop,fitness,**kwargs)
     
        child_pop = create_children(pop,crossover,cross_points=2)
        child_pop = pop_fitness(child_pop,fitness,**kwargs)
    
        #Continue_algorithm flag is evaluated again within this function
        next_pop = selection(pop,child_pop,continue_algorithm,family_competition)
        #Log some stats on the algorithm        
        total_bits = sum(j for i,j in pop)        
        pop_log.append((generation,total_bits, total_bits/len(pop),selection_errors))        


        if np.array_equal(pop,next_pop[0]):
            identical_gen_count += 1
            if identical_gen_count >= 5:
                continue_algorithm=False
        else:    
            pop = next_pop[0]
            selection_errors = next_pop[1]
            generation +=1
            identical_gen_count = 0
    end = time.time() 

    print('Experiment_2X finished...Trial fitness:' + str(pop_log[len(pop_log)-1][2]),flush=True)
    #pop_log.append((end-start))
    return (pop_log,(end-start))
