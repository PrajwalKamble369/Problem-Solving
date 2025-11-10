print('''
Update Element from List:
      l = [20,30,40,50]
      l[0] = 10
      print(i)

      output: 
            [10,30,40,50]
      
    1) insert() : It insert element in list at mentioned index number. And it insert element only know index numbers.
    2) append() : It insert element in last of list.
    3) extend() : It works on elements.It add at last if this element is list it convert to simple numbers or whatever data type.It is insert support for itrable elements.
\n''')

print("Updating List: ")
l = [30,20,30,40,50]
l[0] = 10
print(l)

print()

print("Insert Method:")
li = [2,3,4,5,6,7,8,9,10]
print("Before using insert:",li)
li.insert(0,1)
print("After using insert:",li)

print()
print("append:")
li = [1,2,3,4,6]
print("Before append:",li)
li.append("Prajwal")
print("After append:", li)

print()
print("extend:")
li = [10,20,30,40,50,60]
li1 = [40,50]
print("Before extend:",li)
li.extend(li1)
print("After extend:",li)

l = [1,2,3,4]
l.extend("5")
print(l)