# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()



def palindrom(a):
    if len(a)>=2:
        if a == a[::-1]:
            print('słowo jest palindromem')
        else:
            print('słowo nie jest palindromem')
    else:
        print('Słowo jest zbyt krotkie')

data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    a=str(input('Wpisz słowo a ja sprawdzę czy jest palindromem'))   
else:
    a= data['Ex_6']
palindrom(a)