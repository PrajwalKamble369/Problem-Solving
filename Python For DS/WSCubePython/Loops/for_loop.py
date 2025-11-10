print("""
For Lopp with Range():
      For loop is used for itration.
      range(5)     = start(0) | end(5-1=4) | increment(1)
      range(1,6)   = start(1) | end(6-1=5) | increment(1)
      range(1,6,2) = start(1) | end(6-1=5) | increment(2)

\n""")

print("with 1 parameter")
for i in range(10):
    print(i,end=" ")

print()

print("with 2 parameters")
for n in range(1,10):
    print(n, end=" ")

print()

print("with 3 parameters")
for n in range(1,10,2):
    print(n,end=" ")


print("Printing table of 2")
for n in range(1,11):
    print(f"2 X {n} =",n*2)

print()

print('''
Reverse Case = range(10,0,-1)
\n''')

for n in range(10,0,-1):
    print(n,end=" ")