import random
 
choices = ["stone", "paper", "scissors"]
beats = {"stone": "scissors", "scissors": "paper", "paper": "stone"}
 
user_score = 0
computer_score = 0
round_num = 1
 
print("=== Stone, Paper, Scissors ===")
 
while True:
    user = input(f"\nRound {round_num} - Enter stone/paper/scissors (or exit): ")
 
    if user == "exit":
        break
 
    if user not in choices:
        print("That's not a valid choice, try again.")
        continue
 
    computer = random.choice(choices)
    print(f"You chose {user}, computer chose {computer}")
 
    if user == computer:
        print("It's a draw!")
    elif beats[user] == computer:
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
 
    print(f"Score - You: {user_score}  Computer: {computer_score}")
    round_num += 1
 
print("\nGame over!")
print(f"Final score - You: {user_score}  Computer: {computer_score}")
 
if user_score > computer_score:
    print("You won overall!")
elif computer_score > user_score:
    print("Computer won overall!")
else:
    print("It's a tie overall!")
