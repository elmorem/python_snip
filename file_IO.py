##
##         READING AND WRITING TEXT DATA

with open('file.txt', 'rt') as f:
    data = f.read
    print(data)

with open('file.txt', 'rt') as f:
    for line in f:
        print(line)
## use open() mode 'wt' to write to file
##use open() mode 'at' to append to file

## To redirect the results of a print statement:  
with open('file1.txt', 'wt') as f:
    print('hello, world', file=f)

# If the file does not exist, it is created with this statement
