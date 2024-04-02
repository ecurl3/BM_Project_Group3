'''This file contains the Gale Shapley Algorithm along with any helper functions as needed'''
#!/usr/bin/env python3
import sys

__authors__ = "BM_GROUP_3 coders: Jacob, Tyler, Emily"

# helps determine if selected woman prefers m over current partner or not
def prefers_over_m(preference, m, partner, w):

    for i in range(len(preference[0])):
        if (preference[w][i] == m):
            # w prefers m over partner
            return True
        if (preference[w][i] == partner):
            # w prefers partner over m
            return False
    
    print("Error")
    sys.exit(1)

# this is the Gale_Shapley function
def algo(preference):
    n = len(preference[0])

    # initialize free males and females by setting them to -1
    freeM = [-1] * n
    prefW = [-1] * n

    freeCount = n

    # iterate until there are no more free males
    while (freeCount > 0):

        # start at the first available free male
        m = 0
        for m in range(n):
            if freeM[m] == -1:
                break
        
        # now we iterate through free male's preference list to find first available woman
        i = 0
        while (i < n) and (freeM[m] == -1):

            # first, we set w to the next woman on preference list
            w = preference[m][i]

            # if preffered woman is free, we must engage the two individuals
            if prefW[w - n] == -1:
                # set male to taken
                freeM[m] = 0  
                # decrease available free males count
                freeCount -= 1
                # now engage the two individuals by setting woman's list to m
                prefW[w - n] = m
            else:
            # this means that woman is engaged already, check if woman prefers m over current partner
                
                partner = prefW[w - n]

                if prefers_over_m(preference, m, partner, w):

                    # then break up w's engagement and engage with m
                    prefW[w - n] = m
                    freeM[m] = 0
                    freeM[partner] = -1
            i += 1
    return prefW       
                    


                