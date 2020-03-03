list= [2,4,6,8,1,3,5,7,9]

new_list = [x**2 for x in list]

print(new_list)

 #square is a generator
square = (i*i for i in irange(1000000))
#add the squares
total = 0
for i in square:
    total += i
print(total)