import random
random_number = random.randint(1,10)

for i in range(4):
    user_input = int(input("Emter number from 1 to 10: "))
    
    if random_number == user_input:
        print("Correct You win !")
        break
    
    else:
        print("Wrong Try agin, wish you luck")

        if random_number > user_input:
            print("random number is greater")

        elif random_number < user_input:
            print("random number is lesser")
            