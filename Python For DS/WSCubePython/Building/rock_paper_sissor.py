import random 
l = ["Rock","Paper", "Scissor"]
computer_wins = 0
player_wins = 0

for i in range(5):
    computer_choice = random.choice(l)
    player_choice = input("Enter [Rock or Paper or Scissor]: ")

    if (computer_choice == "Rock" and player_choice == "Paper") or (computer_choice == "Paper" and player_choice == "Scissor") or (computer_choice == "Scissor" and player_choice == "Rock"):
        print(f"Your choice is {player_choice} and computer choice is {computer_choice}, so You win this round !")
        player_wins += 1

    elif computer_choice == player_choice:
        print(f"Your choice is {player_choice} and computer choice is {computer_choice}, so this round is tie !") 

    else:
        print(f"Your choice is {player_choice} and computer choice is {computer_choice}, so You Lose this round !")
        computer_wins += 1

print()

print("--------------------Game is Over---------------------")
print(f"            You won {player_wins} times....         ")
print(f"        Computer won {computer_wins} times....       ")

if player_wins > computer_wins:
    print("      Congratulations You Won the Game  ")

elif player_wins == computer_wins:
    print("           Its a Tie         ")

else:
    print("            You Lose     ")