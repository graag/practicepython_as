# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock
# Discussion
# Concepts for this week:

# While loops
# Infinite loops
# Break statements



c="y"
while c=="y":
    a=str(input("Rock,Scissors,Paper?")) 
    b=str(input("Rock,Scissors,Paper?"))
    if a ==b:
        print('Remis')    
    elif a=='Rock' and b=='Scissors':
        print('Player 1 wins')   
    elif a=='Rock' and b=='Paper':
        print('Player 2 wins')
    elif a=='Scissors' and b=='Rock':
        print('Player 2 wins')
    elif a=='Scissors' and b=='Paper':
        print('Player 1 wins')
    elif a=='Paper' and b=='Rock':
        print('Player 1 wins')
    elif a=='Paper' and b=='Scissors':
        print('Player 2 wins')
    c=str(input("do you want play onece again? y/n"))
        
            
