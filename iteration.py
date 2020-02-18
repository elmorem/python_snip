# You want to implement a new kind of iteration pattern
# Do it with a generator
# this one produces a range of floating point numbers

def frange(start, stop, increment):
    x = start 
    while x < stop:
        yield x
        x += increment

# to use this use it with a for loop like this

for n in frange(0,6,.5):
    print (n)

#  TO ITERATE IN REVERSE
#use the reversed() function
a=[1,2,3,4,5,6,7]

for x in reversed(a):
    print(x+1)

for x in a:
    print(x)

#TAKE A SLICE OF AN ITERATOR
import itertools
def count(n):
    while True:
        yield n
        n +=1

c = count(0)

for x in itertools.islice(c,10,20):
    print(x)

#A METHOD TO ITERATE OVER ALL THE POSSIBLE PERMUTATIONS IN A COLLECTION
items= [1,2,3,4,5,6,7,'a','b','c']
from itertools import permutations
for p in permutations(items):
    print(p)
#if you want a smaller subset of these you use the optional length arg
items= [1,2,3,4,'a','b','c']
for p in permutations(items,3):
    print(p)

#Now i want to try to create a counter for this
#THIS WOULD BE A GOOD WAY TO DO IT!! AND I DID IT BY MYSELF

items= [1,2,3,4,5,'a','b','c']
for count, p in enumerate(permutations(items)):
    print(count, p)
#for a pretty printed verison
    print("this"{} "is permutation #" %p, count )

##
##TO ITERATE OVER A SEQUENCE AND KEEP TRACK OF WHICH ELEMENT IS BEING PROCESSES

items= [1,2,3,4,5,6,7,'a','b','c']
for idx, val in enumerate(items,1):
    print(idx, val)

## BASICALLY, THE MORAL HERE IS THAT IN ALMOST ALL CIRCUMSTANCES, WHEN YOU WANT TO USE A COUNTER, IT IS OFTEN MORE ELEGANT TO USE ENUMERATE

# USE IT HERE TO TRACK LINE NUMBERS FOR FILE
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f,1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line{}: Parse error: {}'format(lineno, e))

parse_data(file.txt)

##ITERATING OVER ITEMS CONTAINED IN MORE THAN ONE SEQUENCE AT A TIME
## NOTE::  IF THE TOTAL NUMBER OF ITEMS IN THELISTS ARE NOT EQUAL, THE SEQUENCE WILL ONLY FULFIL UP TO THE LOWER NUMER

xpts=[1,2,3,4,5,7]
ypts=[34,35,78,99,66,88]
for x,y in zip(xpts,ypts):
    print(x,y)

# YOU CAN OUTPUT IT AS A TUPLE AS FOLLOWS
xpts=[1,2,3,4,5,7]
ypts=[34,35,78,99,66,88]
for x in zip(xpts,ypts):
    print(x)

##  NOTE:  ZIP IS COMMONLY USED WHENEVER YOU NEED TO PAIR DATA TOGETHER THUS
## IT COULD BE USED TO CREATE DICTIONARY ZIPPING TOGETHER COLUMN HEADER AND VALUES
headers=['NAME','SHARES','PRICE']
values=['ACME',100,490]
#A DICTIONARY
s=dict(zip(headers, values))
print(s)

for name,val in zip(headers,values):
    print(name, '=', val)

##FOR THIS PROBLEM, YOU NEED TO PERFORM THE SAME OPERATION ON MANY OBJECTS, BUT THEY ARE IN DIFFERENT CONTAINERS AND YOU DON'T WANT NESTED LOOPS
##   USE ITERTOOLS.CHAIN()

from itertools import chain
a = [1,2,3,4]
b= ['x', 'y', 'z']

for x in chain(a,b):
    print(x)

##a COMMON USAFE IS WHERE YOU NEED TO PERFOMR OPERATIONS ON TWO GROUPS OF ITEMS AT THE SAME TIME AND ONE SET IS ACTIVE AND THE OTHER IS NOT
active=set()
inactive=set()
for item in chain (active, inactive):
    #proces them

