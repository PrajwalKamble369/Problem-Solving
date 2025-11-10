print('''
String :
        1) A string is sequence of characters.
        2) A string can be created by enclosing characters inside a single quote or double-quoat.
        3) Triple quotes are used to represent multiline string.
\n''')


print('''
______________________________________________
|             String Indexing                |
|____________________________________________|
|                      |                     |
|-7 -6 -5 -4 -3 -2 -1  | Negative Indexing   |
|P   R  A  J  W  A  L  | String              |
|0   1  2  3  4  5  6  | Positive Indexing   |
|______________________|_____________________|
\n''')

a = "Welcome to Python Learning Journy"

print("Indexing: ",a[0], "\n")
print("Slicing: ", a[0:7],"\n")
print("Slicing with step (increament case): ",a[0:7:2],"\n")
print("Reverse of String: ",a[-1::-1])