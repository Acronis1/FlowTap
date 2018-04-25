import random
import sys
import os
import math

'''
boys to girls reatio in the long run
i suppose the following things:
    boy(1)/girl(0) birth probability 0.5
    no evolution (only the initial couples have children)
'''
nrcouples=1000                           #the number of couples, if a couple already has a boy i will subtract them
nrboys=0
nrgirls=0
t=0                                      # this will represent the time for iterations, increased by one each time

def child(nrcouples,t):   # the function for calculating the newborn girls and boys
    global nrboys
    global nrgirls
    while t<100 and nrcouples>0:
        for i in range(0,nrcouples):
            birth=random.randint(0,1)    # a child has been born
            if(birth==1):                # the case if the newborn is a boy
                nrcouples-=1
                nrboys+=1
            else:                        #case for a girl
                nrgirls+=1
        t+=1
   # print(nrboys,nrgirls)               #this can be useful to track the nr of children

    return nrboys/nrgirls;


child(nrcouples,t)

#now, this would be just one community, let's create multiple ones and avarage them out ti increase precision:

ratio=0

for i in range (0,50):
    ratio+=child(nrcouples,t)

print("the average is :", ratio/50)

#in conclusion the simulation gives us a ratio of around 1, so the same number of girls and boys are born in this society