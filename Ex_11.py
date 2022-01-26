# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. 
# Take this opportunity to practice using functions, described below.

def get_integer():
    return int(input("Give me a number: "))


n=get_integer()


for x in range(2, n):
    if n % x == 0:
        print(n, "it's not a prime number")
        break
else:
        print(n, 'is a prime number')