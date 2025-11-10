print('''
Tuple Functions:
        1) min()        : It gives minimum value. It is also not inbuild tuple function.
        2) max()        : It gives maximum value. It is also not inbuild tuple function.
        3) count()      : It counts occurence of the perticular element in tuple.
        4) index()      : It gives the index number of element in tuple.
        5) sum(tuple)   : It works on integer and not tuple function it is genral function
\n''')


t = (10,20,20,"a",2.5,[1,2],True,{"a":[10,20]})

t0 = (1,2,3,4,1.1)
print("min():")
print(min(t0))

print()
print("max():")
print(max(t0))

print()

print("count():")
print(t.count(10))

print()

print("index():")
print(t.index([1,2]))

print()

t1 = (1,2)
print("sum:")
print(sum(t1))

