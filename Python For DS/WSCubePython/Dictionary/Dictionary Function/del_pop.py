print('''
del   : It uses keys, we can use without keys but this will remove entire dictonary.
pop() : It uses keys, by default it delelts last element and also printing the deleted element
''')


di = {
      "name": "Python",
      "fees" : 8000,
      "duration" :"2 Months",
      "type": "Programming Language",
      "Liabrary": ["numpy","pandas","seaborn","matplotlib"],
      "year": 2025
      }

del di["fees"]


print("pop():",di.pop("name"))

print()

print(di)