# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:07:15 2018

@author: tomor
"""
import matplotlib.pyplot as plt
import pickle
import numpy as np
from scipy.optimize import curve_fit

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
    
    plt.figure()
    plt.scatter(x=UX[0],y=UX[1],c='blue',marker='o',alpha=0.7,label='UX')
    plt.scatter(x=TWOX[0],y=TWOX[1],c='red',marker='x',label='2X')
    #Try log y to x if this looks silly
    plt.plot(UX[0],fit_func(UX[0],*uxfit_vars),'blue')
    plt.plot(TWOX[0],fit_func(TWOX[0],*twoxfit_vars),'red')
    plt.xlabel('Population Size')
    plt.ylabel('Number of Successes')
    plt.ylim((-1,26))
    plt.legend(loc=4)
    
    #plt.plot(np.unique(TWOX[0]), np.poly1d(np.polyfit(np.log(TWOX[0]), TWOX[1], 1))(np.unique(UX[0])),fmt='r-')
    plt.savefig(filename,bbox_inches='tight',dpi=200)
    plt.show()

if __name__ == '__main__':
    
    with open('CountOnes_UX','rb') as fp:
        CountOnes_UX = pickle.load(fp)
    
    CountOnes_UX_graphdata = get_graph_data(CountOnes_UX)
    
    with open('CountOnes_2X','rb') as fp:
        CountOnes_2X = pickle.load(fp)
    #test=array(CountOnes_UX)
    CountOnes_2X_graphdata = get_graph_data(CountOnes_2X)
    
    plot_min_pop(CountOnes_UX_graphdata,CountOnes_2X_graphdata,'plot1.png')
    
    fit_test = linregress(CountOnes_UX_graphdata[0],CountOnes_UX_graphdata[1])
        
#    Results_DecepTrap_UX = Minimum_Population_UX_Parallel(trap=True)
#    with open('Deceptive_UX','wb') as fp:
#        pickle.dump(Results_DecepTrap_UX,fp)
#    
#    Results_DecepTrap_2X = Minimum_Population_2X_Parallel(trap=True)
#    with open('Deceptive_2X','wb') as fp:
#        pickle.dump(Results_DecepTrap_2X,fp)
#    
#    Results_NonDecepTrap_UX = Minimum_Population_UX_Parallel(trap=True,d=2.5)
#    with open('NonDeceptive_UX','wb') as fp:
#        pickle.dump(Results_NonDecepTrap_UX,fp)
#    
#    Results_NonDecepTrap_2X = Minimum_Population_2X_Parallel(trap=True,d=2.5)
#    with open('NonDeceptive_UX','wb') as fp:
#        pickle.dump(Results_NonDecepTrap_2X,fp)
#    
#    Results_Random_Deceptive_Trap_UX = Minimum_Population_UX_Parallel(trap=True,random_linked=True)
#    with open('Random_Deceptive_UX','wb') as fp:
#        pickle.dump(Results_Random_Deceptive_Trap_UX,fp)
#    
#    Results_Random_Deceptive_Trap_2X = Minimum_Population_2X_Parallel(trap=True,random_linked=True)
#    with open('Random_Deceptive_2X','wb') as fp:
#        pickle.dump(Results_Random_Deceptive_Trap_2X,fp)   
#    
#    Results_Random_NonDeceptive_Trap_UX = Minimum_Population_UX_Parallel(trap=True,random_linked=True,d=2.5)
#    with open('Random_NonDeceptive_UX','wb') as fp:
#        pickle.dump(Results_Random_NonDeceptive_Trap_UX,fp) 
#        
#    Results_Random_NonDeceptive_Trap_2X = Minimum_Population_2X_Parallel(trap=True,random_linked=True,d=2.5)
#    with open('Random_NonDeceptive_2X','wb') as fp:
#        pickle.dump(Results_Random_NonDeceptive_Trap_2X,fp) 