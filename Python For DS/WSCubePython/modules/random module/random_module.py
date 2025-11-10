print("""
Random module can genrate random numbers.
Random module can pick the random values(elements) from list(itrable).
""")

import random

print("randint genrate random value from a given range")
random_value = random.randint(10,100)
print(random_value,"\n")

print("randrange returns a number between given range")
random_number = random.randrange(10,100)
print(random_number,"\n")

print("choice is choose random value from list(itrable)")
a = ["Banana","Apple","Egg","Chicken"]
random_choice = random.choice(a)
print(random_choice,"\n")

print("random genrate value between 0 and 1")
b = random.random()
print(b,"\n")

print("shuffle takes sequence and returns the sequence in a random order")
li = [1,2,3,4,5,6]
random.shuffle(li)
print(li,"\n")

print("uniform returns a random float number between two given parameters")
uni = random.uniform(10,20)
print(uni,"\n")