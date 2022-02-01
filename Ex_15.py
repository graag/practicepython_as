# Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order. For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", type=str, nargs='?')
args = parser.parse_args()

def words_backwords(a):
    b=a.split()
    
    for i in b:
        c=b[::-1]
    return c 


data = None
if args.f:
    with open(args.f, 'r') as f:
        data = json.load(f)
if data == None:
    a=str(input('Wpisz wiele słów'))
else:
    a=data["Ex_15"]

print(words_backwords(a))