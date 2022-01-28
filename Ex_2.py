# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()

data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)

    # for i in data.items():
    #     print(i)

if data==None:
    number=int(input('Podaj liczbę'))
    if number==0:
        print('to jest liczba 0')
    elif number%2 != 0:
        print('to jest liczba nieparzysta')
    else:
        print('to jest liczba parzysta')
else:
    number=data['Ex_2']
    if number==0:
        print('to jest liczba 0')
    elif number%2 != 0:
        print('to jest liczba nieparzysta')
    else:
        print('to jest liczba parzysta')