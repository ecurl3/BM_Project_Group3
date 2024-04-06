'''Contains functions to be called at the start of program execution'''
#!/usr/bin/env python3
import random

__authors__ = "BM_GROUP_3 coders: Jacob, Tyler, Emily"

# print out the engagements after algorithm
def print_engagements_after(engagements):
    nums = len(engagements)

    print("RESULT")
    for i in range(nums):
        # i do 'W{i+nums}' because woman's numbers start from n to 2*n-1
        print(f'M{engagements[i]}: W{i+nums}\tW{i+nums}: M{engagements[i]}')
    
    print("---------------------------------------------------------------------------")

# print out the preferences of each person before algorithm
def print_preferences_before(preference):
    rows, columns = len(preference), len(preference[0])

    # prints out the men's preference list
    print("---------------------------------------------------------------------------")
    print("PREFERENCE LIST")
    for i in range(columns): 
        # this prints out the men's preference list
        print(f'M{i}: ', end='')

        for j in range(columns):

            print(f'W{preference[i][j]} ', end='')
            
        # this prints out the women's prefence list beside men's using \t
        print(f'\tW{i+columns}: ', end='')
        for j in range(columns):
            print(f'M{preference[i+columns][j]} ', end='') # remember that women's preference starts from n to 2*n -1

        print('\n')
    print("---------------------------------------------------------------------------")

    # prints out the women's preference list
    '''print("____WOMEN____")      
    for i in range(columns, rows): # uses range columns -> rows because women's list is n -> 2*n-1
        print(f'W{i}: ', end='')
        for j in range(columns):
            print(f'{preference[i][j]}', end='')
        print('\n')'''
                
                

# generates random preference list given a size from user
def gen_random_preference(n):
    rows, num = 2*n, n 
    preference =[]

    for i in range(rows):
        
        if i < n:
            # then we are adding men's preferences of women (n -> 2*n -1)
            preference.append(random.sample(range(n, 2*n), num))
        else:
            # then we are adding women's preferences of men (0 -> n-1)
            preference.append(random.sample(range(0, n), num))
    
    return preference