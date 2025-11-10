print('''
List Itration :
                # declering list
                l = [10,20,30,50,60] 
                
                # 1st way
                le = len(l)
                for i in range(le):
                    print(i)
                
                # 2nd way
                for i in l:
                    print(i)
      
Printing List in Reverse :
      To print list in reverse the 2nd way will be not used. To get reversed list we always need use range.
      In this range require 3 arguments like 
      range(start, stop, step), 
      so range (length of list -1, -1 ,-1)

                # reverse list itration
                l = [10,20,30,50,60]
                le = len(l)
                for i in range(l-1,-1,-1):
                    print(i)
\n''')

# declearing list
l = [10,20,30,50,60]

# first way
print("List itration using length:")
le = len(l)
for i in range(le):
    print(l[i])

print()
# second way
print("List itration without using length:")
for i in l:
    print(i)

print()

print("Reverse List:")
# declearing list
li = [10,20,30,40,50,60]

leng = len(li)
for i in range(leng-1,-1,-1):
    print(li[i])

print()
print("Reverse List using inbuilt method:")
for i in reversed(l):
    print(i)

print()

print('''
Syntax :
      l = [1,2,3]
      l0 = [4,5,6]
      for i, j zip(l,l0):
        print(i,j)      

itrate over 2+ lists at the same time (zip function)
      it itrate more than one list single time.
      if one list have more elements it print the same length element and ignore excessive elements.
      example : l = [1,2]
                l0 = [3,4,5]
                it will return 1 3
                               2 4

    
\n''')

list1 = [10,20,30,40]
list2 = [3,4,99,77,88]

for i,j in zip(list1,list2):
    print(i,j)

print()
print("Without using zip:")

list_a = [1,2,3,4]
list_b = [7,8,9,10]
len_lista = len(list_a)

for i in range(len_lista):
    print(list_a[i],list_b[i])