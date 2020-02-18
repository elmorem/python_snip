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

