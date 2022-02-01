# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first 
# exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

from random import randrange
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()

def guess_number(b):
    try:
        c='e'
        while c!='exit':
            a=randrange(1,10)
            
            print(a)
            if a==b:
                print('You guess!')
            elif a<b:
                print('Too high')
            elif a>b:
                print('Too low')
            c=input('Do you want exit the game? Write exit')

    except: 
        print('Something went wrong')

data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    b=int(input('Guess the number'))
else:
    b= data['Ex_9']
guess_number(b)