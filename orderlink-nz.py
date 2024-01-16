# Given an array/list of integers, transform this array/list so that each element at index i is the product of all the numbers in the original array/list except the one at i. Implement a function transformArray(arr)/transformList(list).

input = [1, 2, 3, 4, 5]
# output = [120, 60, 40, 30, 24]

a = []
for i in input:
    r = 1
    for j in input:
        if i != j:
            r = r * j
    a.append(r)
print(a)


# Write a function reverseList(list)/reverseArr(arr that reverses a given list without using built-in methods like reverse() in Python or reverse() in JavaScript, and without using len() in Python or lengthOf() in JavaScript. The function should manually calculate the length of the list/array and perform the reversal.

print(input[::-1])