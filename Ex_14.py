# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

# Extras:

# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()



def new_list(old_list):
    new_list=[]
    new_list=set(old_list)
    return list(new_list)


data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    a=[1,1,2,4,4]
    print(new_list(a))
else:
    a=data['Ex_14']
    print(new_list(a))