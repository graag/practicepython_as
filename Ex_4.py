# Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()




def divides(a):
    list1=[]
    for i in range(1,a+1):
        if a%i == 0:
            list1.append(i)

    print('dzielnikiem podanej liczby: '+ str(list1))


data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    a=int(input('Pojad liczbę'))
    divides(a)
    
else:
    divides(data['Ex_4'])