import random 

random_value = random.randint(1,3)
chance = 3

for i in range(chance):

    guess_value = int(input("Enter values from 1 to 3 :"))

    if random_value == guess_value:
        print(f"This is {random_value}, and You Guess Right You won !")

        break

    elif random_value != guess_value:
        print("You can Try again.....") 

else:
    print("Oop's You lose ! Give another Try, Hard Luck...")