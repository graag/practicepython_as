# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
import json
import argparse
import traceback
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()




def divides(a):
    list1=[a]
    for i in range(1,a//2+1):
        if a%i == 0:
            list1.append(i)
    print('dzielnikiem podanej liczby: '+ str(list1))


data = None
try:

    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
except OSError as e:
    traceback.print_exc()
if data is None:
        a=int(input('Pojad liczbę'))
        if a ==0:
            print("Podaj inną liczbę")
        else:   
        
            divides(a)
    
else:
    divides(data['Ex_4'])
