print('''
List :
___________________________________________________________
| List is comma seperated, ordererd, mutable, data type.  |
| It can contain all type of data type as a elements.     |
| The elements of list can be accessed by using indexing. |
| List is declered in square bracket [].                  |
|_________________________________________________________|
\n''')

print('''
Nested List :
      l = [1,2,3,[4,5,6]]
           0 1 1    3     = list indexes
      Now i want 5 in output,
      so i can do
      print(l[3][1])
\n''')

print('''
Mixed List :
      l = [2,3,"Hello",[3,4,5]]
           0 1   2         3    = indexes
      return Hello, so
      priint(l[2])

List Slicing :
      print(l[0:2]) = 0 and 1 index element will be return.
\n''')

print("Creating List \n")

l = [1,2,3.0,4.8,"Prajwal",[1,"ab",1.1,3],{"a":[1,2]},{1,2},(3,4)]


for i in l:
    print(i)

print(reversed(l))
