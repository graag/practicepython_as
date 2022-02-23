# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
import json
import argparse
import traceback
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()


data = None
try:

    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
except OSError as e:
    traceback.print_exc()
if data is None:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    
else:
    a= data['Ex_5a']
    b=data['Ex_5b']
print(set(a).intersection(b))
