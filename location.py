# import phonenumbers
# from phonenumbers import geocoder

# first = phonenumbers.parse("+919845895466")

# print(geocoder.description_for_number(first, 'en'))

def print_alpha_nums(abc_list, num_list):
    for char in abc_list:
        for num in num_list:
            print(char, num)
    return

print_alpha_nums(['a', 'b', 'c'], [1, 2, 3])

num_list = [21,13,19,3,11,5,18]
g = num_list.remove(13)
# num_list[len(num_list) // 2]
print(g)

x = {1,2,3,4,5}
x.add(5)
x.add(6)

print(x)

import numpy as np
    
# a = np.array([1,2,3,4])
# print(a[[False, True, False, False]])


a = np.array([1,2,3])
b = np.array([4,5,6])
c = a*b
d = np.dot(a,b)

print(c, d)
n=5
print([x*2 for x in range(1,n)])


import math 
print(math.pow(2,10)) # prints 2 elevated to the 10th power

print([1,2,3]*3)