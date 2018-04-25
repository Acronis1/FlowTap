import random
import sys
import os
import math

#the same results are easily achived using Microsoft Excel's normaldistribution function

def mean(list):             #defining the mean function
    sum=0
    i=0
    for x in list:
        sum+=x
        i+=1
    return sum/i;

def deviation(list):        #defining the standard deviation function
    squaredsum=0
    j=0
    for x in list:
        squaredsum+=(x-mean(list))**2
        j+=1

    return math.sqrt(squaredsum/(j-1));


mylist=[random.gauss(1000 , 10) for i in range(100)]                        #creating an initial list, which does not neccesarly fulfill all the criteria

while not( 999.5<=mean(mylist)<=1000.5 and 9.9<=deviation(mylist)<=10.1):   #generating distributions until the criterias are filled
    mylist = [random.gauss(1000, 10) for i in range(100)]

print("the mean is: " , mean(mylist))
print("the deviation is: ",deviation(mylist))

'''
if there are duplicate elements, we can create a set of the initial list, which removes the duplicates and 
create a new list of the set.
we are able to check the number of elements again, if it is not over 100 we can create a new distribution.
with the inbuilt gauss function however we will alwaxs get unique elements in our set.
'''

print("length of the list: ",len(mylist))
mylist=list(set(mylist))
print("length of the list after removing duplicates: ",len(mylist),"\n")
print("the elements of the list are: \n")

mylist=sorted(mylist)

for x in mylist:
    print(x)