print('''
Sets:
      It is unordered data type. 
      Set is unindex data type.
      The data inside set can be deleted but not changed.
      Set is mutable data type.
      Set is not support dictionary and list.
      Set doesen't support duplicate data.

    Set Itration:
      s = {1,2,3}
      for i in s:
          print(i)
    set itration not possible using range , it not support indexing
\n''')

s = {"a",2,2.2,True, 2,2,2+2j}
print(s,"\n")

print("Set Itration using for loop:")
for i in s:
    print(i)