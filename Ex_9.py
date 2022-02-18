# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first 
# exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
import json
import argparse
import traceback
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()
a=random.randint(1,9)
count=0


data = None
try:
    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
except OSError as e:
    traceback.print_exc()


while True:
    
    
    if data is None:
        b=input('Guess the number or exit')
    else:
        b= data['Ex_9']
   

    if a==int(b):
        count+=1
        print('You guess and count', count)
        
    elif a<int(b):
        count+=1
        print('Too high')
        
    elif a>int(b):
        count+=1
        print('Too low')
    elif b== 'exit':
        break