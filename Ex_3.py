# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.



import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()

def less5(a):
    for i in a:
        if i <5:
            print(i)
data = None
try:

    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
    if data is None:
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        less5(a)
    
    else:
        less5(data['Ex_3'])
except OSError as e:
    print(e)        