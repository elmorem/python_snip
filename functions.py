#basic recipes related to functions

# WRITING FUNCTIONS THAT ACCEPT ANY NUMBER OF INPUT ARGUMENTS
# USE *
def avg(first, *rest):
    return(first+sum(rest))/1 +len(rest)
# to basically create a sum function
avg(1,2,3,4,)
avg(14,12,23,456,66)  