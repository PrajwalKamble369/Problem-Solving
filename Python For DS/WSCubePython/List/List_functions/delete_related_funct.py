print('''
Functions for Delete Elements from List:
    1) del       : It completly deletes the list.
    2) pop()     : It remove elemet index wise and also returns deleted element.
    3) remove()  : It delete element from list through value.
    4) clear()   : It blanks(clear) entire list.
      \n''')

print("Using del")
l = [20,30,50,60]
print(l)
del l[1]
print(l)

print()

print("Using pop:")

l = [1,2,3,4,5,6]
print(l.pop(1))
print(l)
print(l.pop(),"by default it remove last element of list")

print()
print("Using remove:")
li = [1,3,4,"p","ABC"]
li.remove("p")
print(li)

print()
print("Using clear:")
lis = [1,2,3,4,5]
lis.clear()
print(lis)