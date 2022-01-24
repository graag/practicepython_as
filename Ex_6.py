# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
a=str(input('Wpisz słowo a ja sprawdzę czy jest palindromem'))
if len(a)>=2:
    if a == a[::-1]:
        print('słowo jest palindromem')
    else:
        print('słowo nie jest palindromem')
else:
    print('Słowo jest zbyt krotkie')