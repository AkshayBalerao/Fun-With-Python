import random

options = ("rock", "paper", "scissors")

def user_win():
    global user_score
    user_score += 1
    print("You win this round! 🏆")
    print_score()

def computer_win():
    global computer_score
    computer_score += 1
    print("Computer wins this round! 🏆")
    print_score()

def tie():
    print("It's a tie!")
    print_score()

def print_score():
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
    print("\n")

def declare_winner():
    if user_score == 5:
        print("Congratulations! You are the winner! 🏆🏆🏆")
    elif computer_score == 5:
        print("Computer wins the game. Better luck next time! 🏆🏆🏆")

computer_score = 0
user_score = 0

while computer_score < 5 and user_score < 5:
    player = None
    computer = random.choice(options)
    
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    
    if player == computer:
        tie()
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        user_win()
    else:
        computer_win()

declare_winner()
print("Thanks for playing!")
