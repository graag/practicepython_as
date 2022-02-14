# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
parser.add_argument("-v", "--verbosity", action="count", default=0)
args = parser.parse_args()

data = None
try:
    if args.f:
        with open(args.f, 'r') as f:
            data = json.load(f)
    # print(data)
        for i in data.items():
            print(i)
    
    # Closing file
except OSError as e:
    print(e)


if data is None:                                                                                  
    name=input('What is your name?')
    age=int(input('How old are you?'))
else:
    name = data['name']
    age = data['age']
print(name +' will turn 100 years old in ' +str(2022 +(100-age)))                                                                                                                               
