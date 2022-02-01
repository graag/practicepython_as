# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()

data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    c=[x for x in a if x %2== 0]
else:
    a= data['Ex_7']
    c=[x for x in a if x %2== 0]
print(c)