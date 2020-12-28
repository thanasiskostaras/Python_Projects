# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import math
import copy


# create a function that generates a random list of 0 and 1.
def create_candidate(data):
    return [random.randint(0,1) for _ in range(len(data))]

#print(create_candidate(profit))

# function that swap two random numbers from two random indexes in a list.
def swap_operator(lst,x,y):
    lst[x] ,lst[y] = lst[y], lst[x]
    return lst


# define parameters for the Knapsack problem
    
#weight_1 = []
#weight_2 = []
#weight_3 = []
#profit =[]
#
#for i in range(0,1000):
#    x = random.randint(5,15)
#    y = random.randint(5,15)
#    z = random.randint(5,15)
#    w = random.randint(50,150)
#    
#    weight_1.append(x)
#    weight_2.append(y)
#    weight_3.append(z)
#    profit.append(w)





profit=[142,142,140,110,104,99,94,88,85,74,62,59,56,51]
weight_1=[8,10,14,14,14,14,7,15,13,10,5,12,15,7]
weight_2=[9,6,15,10,9,7,8,15,6,8,10,13,9,8]
weight_3=[8,10,15,10,9,6,12,6,14,5,5,7,13,12]
#defining the RHS of the constraints of every weight.

cap_1=math.ceil(sum(weight_1)/2)
cap_2=math.ceil(sum(weight_2)/2)
cap_3=math.ceil(sum(weight_3)/2)
n=len(profit)
lst=[0 for i in range(n)]
#sol_prof=[]
#best_lst=[]
stop = True

def initial():
    
    # Define an initial solution randomly which does not violate the constraints.
    global lst
    global profit_init
    while True:
        initial_sol = create_candidate(profit)
        LHS_1 = sum([initial_sol * weight_1 for initial_sol, weight_1 in zip(initial_sol,weight_1)])
        LHS_2 = sum([initial_sol * weight_2 for initial_sol, weight_2 in zip(initial_sol,weight_2)])
        LHS_3 = sum([initial_sol * weight_3 for initial_sol, weight_3 in zip(initial_sol,weight_3)])
        if LHS_1 < cap_1 and LHS_2 < cap_2 and LHS_3 < cap_3 :
            lst = copy.deepcopy(initial_sol)
            profit_init=sum([lst * profit for lst, profit in zip(lst,profit)])
            break
        else:
            continue
    
    # return the initial solution and the initial profit for this list.
    return lst, profit_init
    

def HC(lst,profit_init):
    
    # Use local heuristic approach to find the final solution, using as a starting point the initial solution defined above.
    marco = profit_init
    for i in range(100): # simulation run for 1000 iterations
        z =random.randint(0,n-1)
        if lst[z] != 1:
            temp = lst[:]
            # insert at random position a value 1.
            temp[z] = 1
            LHS_1 = sum([temp * weight_1 for temp, weight_1 in zip(temp,weight_1)])
            LHS_2 = sum([temp * weight_2 for temp, weight_2 in zip(temp,weight_2)])
            LHS_3 = sum([temp * weight_3 for temp, weight_3 in zip(temp,weight_3)])
            if LHS_1 <= cap_1 and LHS_2 <= cap_2 and LHS_3 <= cap_3: # check if any constraint is violated.
                x,y = random.randint(0,n-1), random.randint(0,n-1)
                # perfom the swap operator into the new list
                newlist = swap_operator(temp,x,y)
                newprofit = sum([newlist * profit for newlist, profit in zip(newlist,profit)])
                LHS_4 = sum([newlist * weight_1 for newlist, weight_1 in zip(newlist,weight_1)])
                LHS_5 = sum([newlist * weight_2 for newlist, weight_2 in zip(newlist,weight_2)])
                LHS_6 = sum([newlist * weight_3 for newlist, weight_3 in zip(newlist,weight_3)])
                if newprofit >= profit_init and LHS_4 <= cap_1 and LHS_5 <= cap_2 and LHS_6 <= cap_3: # check if the newprofit is greater or equal to the previous profit and the constraints are not violated(again).
                    profit_init = newprofit
                    temp = newlist
                    lst=temp
                else:
                    # do the swap again to return to the previous list.
                    swap_operator(temp,x,y)
                    lst=temp
        else:
            # if the number checked is equal to 1 proceed here.
            LHS_1 = sum([lst * weight_1 for lst, weight_1 in zip(lst,weight_1)])
            LHS_2 = sum([lst * weight_2 for lst, weight_2 in zip(lst,weight_2)])
            LHS_3 = sum([lst * weight_3 for lst, weight_3 in zip(lst,weight_3)])
            if LHS_1 <= cap_1 and LHS_2 <= cap_2 and LHS_3 <= cap_3: # check if any constraint is violated.
                x,y = random.randint(0,n-1), random.randint(0,n-1)
                # do the swap operator 
                newlist = swap_operator(lst,x,y)
                newprofit = sum([newlist * profit for newlist, profit in zip(newlist,profit)])
                LHS_4 = sum([newlist * weight_1 for newlist, weight_1 in zip(newlist,weight_1)])
                LHS_5 = sum([newlist * weight_2 for newlist, weight_2 in zip(newlist,weight_2)])
                LHS_6 = sum([newlist * weight_3 for newlist, weight_3 in zip(newlist,weight_3)])
                if newprofit >= profit_init and LHS_4 <= cap_1 and LHS_5 <= cap_2 and LHS_6 <= cap_3: # check the new profit and the violation of the constraints
                    profit_init = newprofit
                    lst = newlist
                else:
                    # swap the list to the previous positions.
                    swap_operator(lst,x,y)
                
    # return the new list and the best profit
    return marco, profit_init, lst

sol = initial()
print(HC(lst,profit_init))


print(sum([lst * weight_1 for lst, weight_1 in zip(lst,weight_1)]),sum([lst * weight_2 for lst, weight_2 in zip(lst,weight_2)]),sum([lst * weight_3 for lst, weight_3 in zip(lst,weight_3)]))



    







