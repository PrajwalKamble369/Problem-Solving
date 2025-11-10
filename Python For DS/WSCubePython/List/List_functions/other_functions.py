print('''
1) count()   : count the occurance of element.
2) max       : find out hingher value form list and not supported between instances of 'str' and 'int'.
3) min       :  find out lower value form list and not supported between instances of 'str' and 'int'.
4) sort()    : it sort the list and not supported between instances of 'str' and 'int'.
5) reverse() : reverse the list.
6) index()   : it return the index number of specific element.
\n''')

l = [1,2,3,4,5,"Prajwal","Prajwal",1,2,3,3,3,100,5,6,7,8,9,10,11,12]

print("count():",l.count(1))

li = [1,2,3,100,500,1000]
print("max():", max(li))

print("min():",min(li))


l0 = [9,8,7,6,5,4,3,2,1]
l0.sort()
print("sort():",l0)

l1 = l.copy()
l1.reverse()
print("reverse():",l1)

print("index():",l.index("Prajwal"))

