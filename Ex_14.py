# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
def new_list(old_list):
    new_list=[]
    new_list=set(old_list)
    return list(new_list)

a=[1,1,2,4,4]
print(new_list(a))