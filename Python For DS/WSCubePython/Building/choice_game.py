import random

name = input("Pleas Enter Your Name to start: ")

print(f'''

        Hello {name}, Welcome To Guessing Game !
**************************************************************
      <><><><><><><><><><><><><><><><><><<><><>
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      ()()()()()()()()()()()()()()()()()()()()()   

\n''')

values = ["Cricket", "Football","Running","Cards"]
random_value = random.choice(values)

chance = 3

for i in range(chance):
    
    if random_value == "Cricket":
        print("The game related to ball and it is genrally long game time wise")
        guess = input("Guess the game between [Cricket, Football,Running,Cards] ")
        if random_value == guess:
            print(f"Congrats You Guess Correct {random_value}")
        else:
            print("Try Again")
        break

    elif random_value == "Football":
        print("The game have ball and everyone is running in this game")
        guess = input("Guess the game between [Cricket, Football,Running,Cards] ")
        if random_value == guess:
            print(f"Congrats You Guess Correct {random_value}")
        else:
            print("Try Again")

        
    
    else:
     print("Lose")