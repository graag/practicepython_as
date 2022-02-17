# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

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

    # for i in data.items():
    #     print(i)
except OSError as e:
    traceback.print_exc()

try:  
    if data is None:
        number=int(input('Podaj liczbę'))

    else:
        number=data['Ex_2']
except ValueError:
    print("Oops!  That was no valid number.  Try again...")       
    
if number==0:
    print('to jest liczba 0')
elif number%2 != 0:
    print('to jest liczba nieparzysta')
    
else:
    print('to jest liczba parzysta')
            
