import random

guess_count = 0
guess_limit = 3
computer_wins = 0
human_wins = 0

list_computerwins = {"paper beats rock","scissors beats paper", "rock beats scissors"}
list_humanwins = {"paper beats rock","scissors beats paper", "rock beats scissors"}

print("This is a simple game of rock, paper, scissors. The best of three wins! Godspeed!")

while guess_count < guess_limit:
    #take input
    humanguess=input("rock, paper, or scissors? ")
    
    guess_count += 1
    
    if humanguess == 'exit' or humanguess == 'quit':
        break

    if humanguess != 'rock' and humanguess != 'paper' and humanguess != 'scissors':
        print("Please choose a correct answer.")
        continue
    #random computer choice
    computerguess = random.choice(['rock','paper','scissors'])

    #print choices
    print(f"You chose {humanguess}, while the computer chose {computerguess}")

    #same guess
    if humanguess == computerguess:
        guess_count -= 1
        print(f"You both chose {humanguess}, so you have an extra guess! Try again.")
    
    #computer wins
    elif f"{computerguess} beats {humanguess}" in list_computerwins:
        print("Computer wins this round.")
        computer_wins += 1
    
    #human wins
    elif f"{humanguess} beats {computerguess}" in list_humanwins:
        print("You win this round.")
        human_wins += 1

    #update score
    print(f"You have won {human_wins} times, and the computer has won {computer_wins} times.")

if guess_count == guess_limit:
    if human_wins > computer_wins:
        print("You have won the game! Congratulations!")
    else:
        print("You lost!")
