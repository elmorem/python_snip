#basic recipes related to functions

# WRITING FUNCTIONS THAT ACCEPT ANY NUMBER OF INPUT ARGUMENTS
# USE *
def avg(first, *rest):
    return(first+sum(rest))/1 +len(rest)
# to basically create a sum function
avg(1,2,3,4,)
avg(14,12,23,456,66)  

# create functions that accept any numbe of keyword arguments
#  use **

import html

def make_element(name, value, **attrs):
    keyvals= ['%s="%s"' % item for item in attrs.items()]
    attr_str=''.join(keyvals)
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