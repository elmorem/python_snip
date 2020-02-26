##you want to put a wrapper around a function to add extra processing (loggin, timing, etc.)
#the best way to do this is to define a decorator function

import time
from functools import wraps

def timethis(func):
    '''decorator that reports the exectution time.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__,end-start)
        return result
    return wrapper
## an example
@timethis
def countdown(n):
    while n>0:
        n-=1
countdown(10000)   