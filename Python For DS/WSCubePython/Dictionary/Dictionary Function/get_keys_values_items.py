print('''
Dictionary Functions:
      get()    : It returns the values of dictionary by taking keys as a parameters.
      keys()   : It returns the keys of dictionary.
      values() : It returns the values from dictionary.
      items()  : It returns both values and keys from dictionary.
\n''')

di = {
      "name": ["Prajwal","Viraj","Rahul"],
      "sub" : ["Python","C","C++"],
      "diff" :["adv","beg","beg"]
      }

print("get() :",di.get("name"))
print()
print("keys():",di.keys())
print()
print("values():",di.values())
print()
print("items():",di.items())
print()

print("keys() using for loop:")
for k in di.keys():
    print(k)

print()
print("values() using for loop:")
for v in di.values():
    print(v)

print()
print("items() using for loop:")
for k,v in di.items():
    print("keys:",k,"|","values:",v)