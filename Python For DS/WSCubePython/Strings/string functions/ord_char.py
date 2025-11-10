print('''
chr() : It requires parameter. We pass integer value as an parameter and returns character value accordingly.
ord() : It requires parameter. We pass charcater and return number accordingly.
''')

print(chr(99))

for i in range(1,1000):
    print(i,chr(i),end=" ")

print(chr(65))

print(ord("A"))