# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

import json
import argparse
import traceback
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()
def get_integer():
    while True:
        try:
            a= int(input("Give me a number: "))
            a=int(a)
            break
            
        except ValueError:
            print('Valid number, please') 
            continue
    return a
def prime_number(a):
    for x in range(2, a//2):
        if a % x == 0:
            print(a, "it's not a prime number")
            break
    else:
            print(a, 'is a prime number')

data = None
try:
    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
except OSError as e:
    traceback.print_exc()
if data is None:
    a=get_integer()
    
else:
     a= data['Ex_11']
prime_number(a)








