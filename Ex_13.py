# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. 
# Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. 
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()




def fib(n):
    a,b=0,1
    for i in range(1,n+1):
        print(a)
        
        a, b = b, a+b
        
    print()
data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data is None:
    n=int(input("how many Fibonnaci numbers to generate?"))
    if n>=1:
        print(fib(n))
    else:
        print('Error')
else:
    n= data['Ex_13']    
    print(fib(n))