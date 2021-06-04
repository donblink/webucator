import random

def main():
    print("===================================")
    print("\n")
    game = ("rock", "paper", "scissor")
    computer_choice = random.choice(game)
    user_choice = input("1 for Rock, 2 for Paper, 3 for Scissors:")
    print("Computer: " + computer_choice )
    print("User    : " + game[int(user_choice)-1])
    print("\n")
    print("===================================")
    

main()    