# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
# def new_list(elements):

import random 
a = list(set([random.randint(0,100) for x in range(random.randint(3,6))]))

def new_list(a):
    new_a= [a[0],a[-1]]
    return new_a

print(new_list(a))