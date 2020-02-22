## program

import requests 
   element='<{name}{attrs}>{value}</{name}>'.format(
                name=name,
                attrs=attr_str,
                value=html.escape(value))
    return element

#example
make_element('item', 'Albatross', size='large', quantity=6)

#WRITING FUNCTIONS THAT ACCEPT ONLY KEYWORD ARGS
# function ONLY accepts certain keyword arguments
# to do this, use either a single unnamed * argument OR place the keyword arguments after a * argument

def recv(maxsize, *,block):
    'recieves a message'
    pass
recv(1024, True)
#this results in a Type Error
recv(1024, block=True)
#returns ok

### This can also be used to specify keyword argument sthat accept a varying number of postitional args.

def minimum(*values, clip=None):
    m=min(values)
    if clip is not None:
        m=clip if clip> m else m
    return m
minimum(1,5,2,-5,10)
#returns-5
minimum(1,5,2,-5,10, clip=0)

#returns 0

# attaching metadata to function arguments
# THESE ARE CALLED FUNCTION ANNOTATION and they help later programmers understand how it is to be used
#they are stored in the functions __annotations__ attribute

def add(x:int, y:int) ->int:
    return x+y

help(add)

# returns
# Help on function add in module __main__:

# add(x:int, y:int) -> int

## RETURNING MULTIPLE VALUES FROM A FUNCTION
#to do this, you simply return a tuple

def myfun():
    return 1,2,3
a,b,c,=myfun()
# >>>a
# 1
# >>>b
# 2
# >>>c
# 3
# >>>a,b,c
# (1,2,3)

## YOU WANT TO DEFINE A FUNCTION WHERE ONE OR MORE OF THE ARGS ARE OPTIONAL AND HAVE DEFAULT VALUE 
# defining functions with default  arguments is a bit tricky.
# first, the calues assigned as a defailt are bound only ONCE at definition.
# THUS, changing this in the body of the function or at call time will have no effect
# IMPORTANT values assigned as defailts should always be immutable objects

def spam(a,b=42):
    print(a,b)
spam(1)
spam(1,2)

#ONE LINE FUNCTIONS
#use lambda

add= lambda x,y: x+y
add(2,3)
#returns 5

##You have an anonymous function BUT you need to capture the values of certain variables at the time of definition
# to do this, you must use the formulation x=x

##NOT LIKE THIS
x=10
a=lambda y: x+y
x=20
b=lambda y: x+y
#for this, both a(10) and b(10) return 30
# THUS LIKE THIS
x=10
a=lambda y, x=x: x+y
x=20