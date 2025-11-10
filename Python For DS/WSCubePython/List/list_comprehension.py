print('''
List Comprehenssion:
       List comprehension is a way to create a list.
       It shorter way to append multiple values in a list.
       In this the code is compressed.

    Syntax of List Comprehension:
      [expression for item in list]        
\n''')

# creating balank list
print("Creating a Blank List:")
l = []
for i in range(1,101):
    l.append(i)
print("List without List comprehension:",l,"\n")

li = [i for i in range(101,201)]
print("List created by 'List Comprehesion':",li,"\n")

fl = [ i for i in range(101,201) if i%2 == 0]
print("Condition in List Comprehension:",fl,"\n")

s = "Hello"
d = [g for g in s]
print("string to list",d)