print('''
Set Functions:
      set()     : It is used to declare set or convert list or tuple to set or other.
      update()  : It add element form itratble to set.
      add()     : We can add new element in set using add.
      pop()     : It remove the element from set. It randomly delete element from set.
      remove()  : It remove element from the set by taking element. It gives error if element not present in set.
      clear()   : It clear element the set. and return "set()".
      discard() : It remove the elemet from set. It doesent give error if element not present in set.

\n''')


l = [10,20,30]
print("set():")
s = set(l)
print(s,"\n")

print("add():")
s.add(2)
print(s,"\n")

print("pop():")
s.pop()
print(s,"\n")

print("update():")
s.update([1,2])
print(s,"\n")


print("discard():")
s.discard(2)
print(s,"\n")

print("remove():")
s.remove(1)
print(s,"\n")

print("clear()")
s.clear()
print(s)


s.update([10,20,30,40,50])
print(s)



