print('''
Program to convert string to a list:
      we will use split() : this will split string by space.
\n''')

sentence = input("Enter the Value: ")

split_sentence = sentence.split()
print(split_sentence)

blank = []

for a in range(1,4):
    n = input("Enter The sentence "+ str(a)+":")
    blank.append(n)
print(blank)

