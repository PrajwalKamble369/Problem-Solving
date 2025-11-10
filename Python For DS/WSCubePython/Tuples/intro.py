print('''
Tuples:
      Tuple is orderd data type and tuple is immutable.
      Tuple should have more than one elements.
      Tuple is faster than list and dictionary.


    Creating Tuple:
       t = (20,30,40,50)
    
    Accessing Tuple:
       print(t[0]) => 20
      
    Tuple itration:
      for i in t:
        print(i)
      l = len(t)
      for i in range(l):
        print(t[i])      
\n''')


print("Creating Tuple:")
t = (10,20,20,"a",2.5,[1,2],True,{"a":[10,20]})
print(t,"\n")

print("Accessing element of Tuple:")
print(t[0],"\n")

print("Itrating tuple without range:")
for i in t:
    print(i)

print()
print("Itrating tuple with range:")
l = len(t)
for i in range(l):
    print(t[i])