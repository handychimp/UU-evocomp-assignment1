# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:07:15 2018

@author: tomor
"""
import matplotlib.pyplot as plt
import pickle
import numpy as np
from scipy.optimize import curve_fit
from operator import itemgetter
import pandas as pd
from pandas.plotting import table

def fit_func(x,a,c):
    return a*np.log(x) + c

def get_graph_data(Results):
    Results_pop = []
    Results_successes = []
    for i in range(0,len(Results)):
        pop = Results[i][0]
        success_counter = 0
        for j in range(0,len(Results[i][1])):
            if Results[i][1][j][0][len(Results[i][1][j][0])-1][2]==100:
                success_counter += 1
        
        Results_pop.append(pop)
        Results_successes.append(success_counter)
    
    return (Results_pop,Results_successes)


    
def plot_min_pop(UX,TWOX,filename):
    uxfit_vars,pcov_ux=curve_fit(fit_func,UX[0],UX[1])
    twoxfit_vars,pcov_ux=curve_fit(fit_func,TWOX[0],TWOX[1])
    max_pop = max(UX[0] + TWOX[0])
    plt.figure()
    plt.scatter(x=UX[0],y=UX[1],c='blue',marker='o',alpha=0.7,label='UX')
    plt.scatter(x=TWOX[0],y=TWOX[1],c='red',marker='x',label='2X')
    #Try log y to x if this looks silly
    plt.plot(range(0,max_pop,10),fit_func(range(0,max_pop,10),*uxfit_vars),'blue')
    plt.plot(range(0,max_pop,10),fit_func(range(0,max_pop,10),*twoxfit_vars),'red')
    plt.xlabel('Population Size')
    plt.ylabel('Number of Successes')
    plt.ylim((-1,26))
    plt.legend(loc=4)
    
    #plt.plot(np.unique(TWOX[0]), np.poly1d(np.polyfit(np.log(TWOX[0]), TWOX[1], 1))(np.unique(UX[0])),fmt='r-')
    plt.savefig(filename,bbox_inches='tight',dpi=200)
    plt.show()
    
def plot_tables(table_dict,filename):
    df = pd.DataFrame.from_dict(table_dict, orient='index')
    
    ax = plt.subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis

    table(ax, df)  # where df is your data frame
    plt.savefig(filename,bbox_inches='tight',dpi=250)
    plt.show()

def get_fixed_pop_data(Results):
    counting_ones_stats_UX = {}
    counting_ones_stats_2X = {}
    deceptive_stats_UX = {}    
    deceptive_stats_2X = {}
    nondeceptive_stats_UX = {}
    nondeceptive_stats_2X = {}
    random_deceptive_stats_UX = {}
    random_deceptive_stats_2X = {}
    random_nondeceptive_stats_UX = {}
    random_nondeceptive_stats_2X = {}
    
    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[0][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[0][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[0][0][i][2])
        sel_errors.append(Fitness_Results[0][0][i][3])
    counting_ones_stats_UX['generation'] = generation
    counting_ones_stats_UX['bit_prop'] = bit_proportion
    counting_ones_stats_UX['mean_fitness'] = mean_fitness
    counting_ones_stats_UX['sel_errors'] = sel_errors
    
    
    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[1][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[1][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[1][0][i][2])
        sel_errors.append(Fitness_Results[1][0][i][3])
    counting_ones_stats_2X['generation'] = generation
    counting_ones_stats_2X['bit_prop'] = bit_proportion
    counting_ones_stats_2X['mean_fitness'] = mean_fitness
    counting_ones_stats_2X['sel_errors'] = sel_errors


    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[2][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[2][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[2][0][i][2])
        sel_errors.append(Fitness_Results[2][0][i][3])
    deceptive_stats_UX['generation'] = generation
    deceptive_stats_UX['bit_prop'] = bit_proportion
    deceptive_stats_UX['mean_fitness'] = mean_fitness
    deceptive_stats_UX['sel_errors'] = sel_errors        
    
    
    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[3][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[3][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[3][0][i][2])
        sel_errors.append(Fitness_Results[3][0][i][3])
    deceptive_stats_2X['generation'] = generation
    deceptive_stats_2X['bit_prop'] = bit_proportion
    deceptive_stats_2X['mean_fitness'] = mean_fitness
    deceptive_stats_2X['sel_errors'] = sel_errors


    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[4][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[4][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[4][0][i][2])
        sel_errors.append(Fitness_Results[4][0][i][3])
    nondeceptive_stats_UX['generation'] = generation
    nondeceptive_stats_UX['bit_prop'] = bit_proportion
    nondeceptive_stats_UX['mean_fitness'] = mean_fitness
    nondeceptive_stats_UX['sel_errors'] = sel_errors


    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[5][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[5][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[5][0][i][2])
        sel_errors.append(Fitness_Results[5][0][i][3])
    nondeceptive_stats_2X['generation'] = generation
    nondeceptive_stats_2X['bit_prop'] = bit_proportion
    nondeceptive_stats_2X['mean_fitness'] = mean_fitness
    nondeceptive_stats_2X['sel_errors'] = sel_errors                


    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[6][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[6][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[6][0][i][2])
        sel_errors.append(Fitness_Results[6][0][i][3])
    random_deceptive_stats_UX['generation'] = generation
    random_deceptive_stats_UX['bit_prop'] = bit_proportion
    random_deceptive_stats_UX['mean_fitness'] = mean_fitness
    random_deceptive_stats_UX['sel_errors'] = sel_errors
    

    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[7][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[7][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[7][0][i][2])
        sel_errors.append(Fitness_Results[7][0][i][3])
    random_deceptive_stats_2X['generation'] = generation
    random_deceptive_stats_2X['bit_prop'] = bit_proportion
    random_deceptive_stats_2X['mean_fitness'] = mean_fitness
    random_deceptive_stats_2X['sel_errors'] = sel_errors
    
    
    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[8][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[8][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[8][0][i][2])
        sel_errors.append(Fitness_Results[8][0][i][3])
    random_nondeceptive_stats_UX['generation'] = generation
    random_nondeceptive_stats_UX['bit_prop'] = bit_proportion
    random_nondeceptive_stats_UX['mean_fitness'] = mean_fitness
    random_nondeceptive_stats_UX['sel_errors'] = sel_errors


    generation =[]
    bit_proportion =[]
    mean_fitness=[]
    stdev=[]
    sel_errors=[]
    for i in range(0,len(Fitness_Results[9][0])):
        generation.append(i)
        bit_proportion.append((Fitness_Results[9][0][i][1])/25000)
        mean_fitness.append(Fitness_Results[9][0][i][2])
        sel_errors.append(Fitness_Results[9][0][i][3])
    random_nondeceptive_stats_2X['generation'] = generation
    random_nondeceptive_stats_2X['bit_prop'] = bit_proportion
    random_nondeceptive_stats_2X['mean_fitness'] = mean_fitness
    random_nondeceptive_stats_2X['sel_errors'] = sel_errors
    
    Results=[]
    Results.append(counting_ones_stats_UX)
    Results.append(counting_ones_stats_2X)
    Results.append(deceptive_stats_UX) 
    Results.append(deceptive_stats_2X)
    Results.append(nondeceptive_stats_UX)
    Results.append(nondeceptive_stats_2X)
    Results.append(random_deceptive_stats_UX)
    Results.append(random_deceptive_stats_2X)
    Results.append(random_nondeceptive_stats_UX)
    Results.append(random_nondeceptive_stats_2X)
    
    return Results
    
if __name__ == '__main__':
    
    with open('CountOnes_UX','rb') as fp:
        CountOnes_UX = pickle.load(fp)
    
    CountOnes_UX_graphdata = get_graph_data(CountOnes_UX)
    
    with open('CountOnes_2X','rb') as fp:
        CountOnes_2X = pickle.load(fp)
    #test=array(CountOnes_UX)
    CountOnes_2X_graphdata = get_graph_data(CountOnes_2X)
    
    plot_min_pop(CountOnes_UX_graphdata,CountOnes_2X_graphdata,'plot_countones.png')
    
        
    with open('Deceptive_UX','rb') as fp:
        Deceptive_UX=pickle.load(fp)
    Deceptive_UX_graphdata=get_graph_data(Deceptive_UX)
    
    with open('Deceptive_2X','rb') as fp:
        Deceptive_2X=pickle.load(fp)
    Deceptive_2X_graphdata = get_graph_data(Deceptive_2X)

    plot_min_pop(Deceptive_UX_graphdata,Deceptive_2X_graphdata,'plot_deceptive.png')

    
    with open('NonDeceptive_UX','rb') as fp:
        NonDeceptive_UX=pickle.load(fp)
    NonDeceptive_UX_graphdata = get_graph_data(NonDeceptive_UX)
    
    with open('NonDeceptive_2X','rb') as fp:
        NonDeceptive_2X=pickle.load(fp)
    NonDeceptive_2X_graphdata = get_graph_data(NonDeceptive_2X)

    plot_min_pop(NonDeceptive_UX_graphdata,NonDeceptive_2X_graphdata,'plot_nondeceptive.png')

    
    with open('Random_Deceptive_UX','rb') as fp:
        DeceptiveRandom_UX=pickle.load(fp)
    DeceptiveRandom_UX_graphdata = get_graph_data(DeceptiveRandom_UX)
    
    with open('Random_Deceptive_2X','rb') as fp:
        DeceptiveRandom_2X=pickle.load(fp)   
    DeceptiveRandom_2X_graphdata = get_graph_data(DeceptiveRandom_2X)
    
    plot_min_pop(DeceptiveRandom_UX_graphdata,DeceptiveRandom_2X_graphdata,'plot_deceptiverandom.png')
    
    
    with open('Random_NonDeceptive_UX','rb') as fp:
        NonDeceptiveRandom_UX=pickle.load(fp) 
    NonDeceptiveRandom_UX_graphdata = get_graph_data(NonDeceptiveRandom_UX)
        
    with open('Random_NonDeceptive_2X','rb') as fp:
        NonDeceptiveRandom_2X=pickle.load(fp) 
    NonDeceptiveRandom_2X_graphdata = get_graph_data(NonDeceptiveRandom_2X)
    
    plot_min_pop(NonDeceptiveRandom_UX_graphdata,NonDeceptiveRandom_2X_graphdata,'plot_nondeceptiverandom.png')
    
    with open('Fitness_Results_250Pop','rb') as fp:
        Fitness_Results = pickle.load(fp) 
        
    Fitness_graphdata = get_fixed_pop_data(Fitness_Results)
       
    plt.figure()
    plt.scatter(x=Fitness_graphdata[0]['generation'],y=Fitness_graphdata[0]['bit_prop'],alpha=0.7,label='Ones UX')
    plt.scatter(x=Fitness_graphdata[1]['generation'],y=Fitness_graphdata[1]['bit_prop'],alpha=0.7,label='Ones 2X')
    plt.xlabel('Generation')
    plt.ylabel('Bit Proportion')
    plt.legend(loc=4)
    plt.savefig('bitprop_counting_ones.png',bbox_inches='tight',dpi=200)
    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[2]['generation'],y=Fitness_graphdata[2]['bit_prop'],alpha=0.7,label='DT UX')
#    plt.scatter(x=Fitness_graphdata[3]['generation'],y=Fitness_graphdata[3]['bit_prop'],alpha=0.7,label='DT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Bit Proportion')
#    plt.legend(loc=4)
#    plt.savefig('bitprop_deceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[4]['generation'],y=Fitness_graphdata[4]['bit_prop'],alpha=0.7,label='NDT UX')
#    plt.scatter(x=Fitness_graphdata[5]['generation'],y=Fitness_graphdata[5]['bit_prop'],alpha=0.7,label='NDT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Bit Proportion')
#    plt.legend(loc=4)
#    plt.savefig('bitprop_nondeceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#
#    
#    plt.scatter(x=Fitness_graphdata[6]['generation'],y=Fitness_graphdata[6]['bit_prop'],alpha=0.7,label='DT-RL UX')
#    plt.scatter(x=Fitness_graphdata[7]['generation'],y=Fitness_graphdata[7]['bit_prop'],alpha=0.7,label='DT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Bit Proportion')
#    plt.legend(loc=4)
#    plt.savefig('bitprop_deceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    
#    plt.scatter(x=Fitness_graphdata[8]['generation'],y=Fitness_graphdata[8]['bit_prop'],alpha=0.7,label='NDT-RL UX')
#    plt.scatter(x=Fitness_graphdata[9]['generation'],y=Fitness_graphdata[9]['bit_prop'],alpha=0.7,label='NDT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Bit Proportion')
#    plt.legend(loc=4)
#    plt.savefig('bitprop_nondeceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
    
    plt.figure()
    plt.scatter(x=Fitness_graphdata[0]['generation'],y=Fitness_graphdata[0]['mean_fitness'],alpha=0.7,label='Ones UX')
    plt.scatter(x=Fitness_graphdata[1]['generation'],y=Fitness_graphdata[1]['mean_fitness'],alpha=0.7,label='Ones 2X')
    plt.xlabel('Generation')
    plt.ylabel('Mean Fitness')
    plt.legend(loc=4)
    plt.savefig('meanfitness_counting_ones.png',bbox_inches='tight',dpi=200)
    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[2]['generation'],y=Fitness_graphdata[2]['mean_fitness'],alpha=0.7,label='DT UX')
#    plt.scatter(x=Fitness_graphdata[3]['generation'],y=Fitness_graphdata[3]['mean_fitness'],alpha=0.7,label='DT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Mean Fitness')
#    plt.legend(loc=4)
#    plt.savefig('meanfitness_deceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[4]['generation'],y=Fitness_graphdata[4]['mean_fitness'],alpha=0.7,label='NDT UX')
#    plt.scatter(x=Fitness_graphdata[5]['generation'],y=Fitness_graphdata[5]['mean_fitness'],alpha=0.7,label='NDT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Mean Fitness')
#    plt.legend(loc=4)
#    plt.savefig('meanfitness_nondeceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#
#    
#    plt.scatter(x=Fitness_graphdata[6]['generation'],y=Fitness_graphdata[6]['mean_fitness'],alpha=0.7,label='DT-RL UX')
#    plt.scatter(x=Fitness_graphdata[7]['generation'],y=Fitness_graphdata[7]['mean_fitness'],alpha=0.7,label='DT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Mean Fitness')
#    plt.legend(loc=4)
#    plt.savefig('meanfitness_deceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    
#    plt.scatter(x=Fitness_graphdata[8]['generation'],y=Fitness_graphdata[8]['mean_fitness'],alpha=0.7,label='NDT-RL UX')
#    plt.scatter(x=Fitness_graphdata[9]['generation'],y=Fitness_graphdata[9]['mean_fitness'],alpha=0.7,label='NDT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Mean Fitness')
#    plt.legend(loc=4)
#    plt.savefig('meanfitness_nondeceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
    
    plt.figure()
    plt.scatter(x=Fitness_graphdata[0]['generation'],y=Fitness_graphdata[0]['sel_errors'],alpha=0.7,label='Ones UX')
    plt.scatter(x=Fitness_graphdata[1]['generation'],y=Fitness_graphdata[1]['sel_errors'],alpha=0.7,label='Ones 2X')
    plt.xlabel('Generation')
    plt.ylabel('Selection Errors')
    plt.legend(loc=4)
    plt.savefig('selerrors_counting_ones.png',bbox_inches='tight',dpi=200)
    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[2]['generation'],y=Fitness_graphdata[2]['sel_errors'],alpha=0.7,label='DT UX')
#    plt.scatter(x=Fitness_graphdata[3]['generation'],y=Fitness_graphdata[3]['sel_errors'],alpha=0.7,label='DT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Selection Errors')
#    plt.legend(loc=4)
#    plt.savefig('selerrors_deceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    plt.scatter(x=Fitness_graphdata[4]['generation'],y=Fitness_graphdata[4]['sel_errors'],alpha=0.7,label='NDT UX')
#    plt.scatter(x=Fitness_graphdata[5]['generation'],y=Fitness_graphdata[5]['sel_errors'],alpha=0.7,label='NDT 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Selection Errors')
#    plt.legend(loc=4)
#    plt.savefig('selerrors_nondeceptive.png',bbox_inches='tight',dpi=200)
#    plt.show()
#
#    
#    plt.scatter(x=Fitness_graphdata[6]['generation'],y=Fitness_graphdata[6]['sel_errors'],alpha=0.7,label='DT-RL UX')
#    plt.scatter(x=Fitness_graphdata[7]['generation'],y=Fitness_graphdata[7]['sel_errors'],alpha=0.7,label='DT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Selection Errors')
#    plt.legend(loc=4)
#    plt.savefig('selerrors_deceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
#    
#    
#    plt.scatter(x=Fitness_graphdata[8]['generation'],y=Fitness_graphdata[8]['sel_errors'],alpha=0.7,label='NDT-RL UX')
#    plt.scatter(x=Fitness_graphdata[9]['generation'],y=Fitness_graphdata[9]['sel_errors'],alpha=0.7,label='NDT-RL 2X')
#    plt.xlabel('Generation')
#    plt.ylabel('Selection Errors')
#    plt.legend(loc=4)
#    plt.savefig('selerrors_nondeceptive_random.png',bbox_inches='tight',dpi=200)
#    plt.show()
    
    counting_ones={}
    
    counting_ones_UX = {}
    counting_ones_UX["Min_Pop"]=330
    total_generations = 0
    for i in range(0,25):
        total_generations += len(CountOnes_UX[11][1][i][0])
        print(len(CountOnes_UX[11][1][i][0]))
    counting_ones_UX["Avg_Generations"]= total_generations/25
    counting_ones_UX["Avg_Fitness_Evals"] = counting_ones_UX["Avg_Generations"]*counting_ones_UX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += CountOnes_UX[11][1][i][1]
        print(CountOnes_UX[11][1][i][1])
    counting_ones_UX["Avg_CPU_Time"]=total_cpu_time/25
    
    counting_ones_2X = {}
    counting_ones_2X["Min_Pop"]=160
    total_generations = 0
    for i in range(0,25):
        total_generations += len(CountOnes_2X[4][1][i][0])
        print(len(CountOnes_2X[4][1][i][0]))
    counting_ones_2X["Avg_Generations"]= total_generations/25
    counting_ones_2X["Avg_Fitness_Evals"] = counting_ones_2X["Avg_Generations"]*counting_ones_2X["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += CountOnes_2X[4][1][i][1]
        print(CountOnes_2X[4][1][i][1])
    counting_ones_2X["Avg_CPU_Time"]=total_cpu_time/25  
    
    counting_ones["UX"]=counting_ones_UX
    counting_ones["2X"]=counting_ones_2X
    
    
    deceptive_trap={}
    
    UX = {}
    UX["Min_Pop"]=1220
    total_generations = 0
    for i in range(0,25):
        total_generations += len(Deceptive_UX[12][1][i][0])
        print(len(Deceptive_UX[12][1][i][0]))
    UX["Avg_Generations"]= total_generations/25
    UX["Avg_Fitness_Evals"] = UX["Avg_Generations"]*UX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += Deceptive_UX[12][1][i][1]
        print(Deceptive_UX[12][1][i][1])
    UX["Avg_CPU_Time"]=total_cpu_time/25
    
    TWOX = {}
    TWOX["Min_Pop"]=610
    total_generations = 0
    for i in range(0,25):
        total_generations += len(Deceptive_2X[11][1][i][0])
        print(len(Deceptive_2X[11][1][i][0]))
    TWOX["Avg_Generations"]= total_generations/25
    TWOX["Avg_Fitness_Evals"] = TWOX["Avg_Generations"]*TWOX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += Deceptive_2X[11][1][i][1]
        print(Deceptive_2X[11][1][i][1])
    TWOX["Avg_CPU_Time"]=total_cpu_time/25  
    
    deceptive_trap["UX"]=UX
    deceptive_trap["2X"]=TWOX
    
    
    nondeceptive_trap={}
    
    UX = {}
    UX["Min_Pop"]=610
    total_generations = 0
    for i in range(0,25):
        total_generations += len(NonDeceptive_UX[11][1][i][0])
        print(len(NonDeceptive_UX[11][1][i][0]))
    UX["Avg_Generations"]= total_generations/25
    UX["Avg_Fitness_Evals"] = UX["Avg_Generations"]*UX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += NonDeceptive_UX[11][1][i][1]
        print(NonDeceptive_UX[11][1][i][1])
    UX["Avg_CPU_Time"]=total_cpu_time/25
    
    TWOX = {}
    TWOX["Min_Pop"]=320
    total_generations = 0
    for i in range(0,25):
        total_generations += len(NonDeceptive_2X[5][1][i][0])
        print(len(NonDeceptive_2X[5][1][i][0]))
    TWOX["Avg_Generations"]= total_generations/25
    TWOX["Avg_Fitness_Evals"] = TWOX["Avg_Generations"]*TWOX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += NonDeceptive_2X[5][1][i][1]
        print(NonDeceptive_2X[5][1][i][1])
    TWOX["Avg_CPU_Time"]=total_cpu_time/25  
    
    nondeceptive_trap["UX"]=UX
    nondeceptive_trap["2X"]=TWOX
    
    random_deceptive_trap={}
    
    UX = {}
    UX["Min_Pop"]=None
    total_generations = None
    UX["Avg_Generations"]= None
    UX["Avg_Fitness_Evals"] = None
    UX["Avg_CPU_Time"]= None
    
    TWOX = {}
    TWOX["Min_Pop"]=None
    TWOX["Avg_Generations"]= None
    TWOX["Avg_Fitness_Evals"] = None
    TWOX["Avg_CPU_Time"]=None
    
    random_deceptive_trap["UX"]=UX
    random_deceptive_trap["2X"]=TWOX
    
    
    random_nondeceptive_trap={}
    
    UX = {}
    UX["Min_Pop"]=None
    UX["Avg_Generations"]= None
    UX["Avg_Fitness_Evals"] = None
    UX["Avg_CPU_Time"]=None
    
    TWOX = {}
    TWOX["Min_Pop"]=340
    total_generations = 0
    for i in range(0,25):
        total_generations += len(NonDeceptiveRandom_2X[10][1][i][0])
        print(len(NonDeceptiveRandom_2X[10][1][i][0]))
    TWOX["Avg_Generations"]= total_generations/25
    TWOX["Avg_Fitness_Evals"] = TWOX["Avg_Generations"]*TWOX["Min_Pop"]
    total_cpu_time = 0
    for i in range(0,25):
        total_cpu_time += NonDeceptiveRandom_2X[10][1][i][1]
        print(NonDeceptiveRandom_2X[10][1][i][1])
    TWOX["Avg_CPU_Time"]=total_cpu_time/25  
    
    random_nondeceptive_trap["UX"]=UX
    random_nondeceptive_trap["2X"]=TWOX
    
    plot_tables(counting_ones,'table_counting_ones.png')
    plot_tables(deceptive_trap,'table_deceptive_trap.png')
    plot_tables(nondeceptive_trap,'table_nondeceptive_trap.png')
    plot_tables(random_deceptive_trap,'table_random_deceptive_trap.png')
    plot_tables(random_nondeceptive_trap,'table_random_nondeceptive_trap.png')
    