import random

print("===== ROCK PAPER SCISSORS GAME =====")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    # User input
    user = input("\nEnter Rock, Paper, or Scissors: ").lower()

    if user not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        continue

    # Computer choice
    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    # Game logic
    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    # Display scores
    print("\nScore:")
    print("You:", user_score)
    print("Computer:", computer_score)

    # Play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\n===== FINAL SCORE =====")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("Congratulations! You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("The game ended in a tie.")

print("Thanks for playing!")
