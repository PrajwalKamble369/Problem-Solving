print("""
Key Points :
            1) If statement
            2) If else statement
            3) If elif else statement
\n""")

print("""
If Statemet:
      
if [conditional expression]:
      [statement(s) to execute]


Example :
      
a = 2
if a % 2 == 0:
      print("Even Number")
\n""")

a = eval(input("Enter any number: "))
print("This will give the output only if the condition statisfied\n")
if a % 2 ==0:
    print(f"{a} is a even number")


print("""
If else statement :
      
if [conditional expression]:
      [statement(s) to execute]
else:
    [statement(s) to execute]
      
Example:

a = 2      
if a % 2 == 0:
    print("It is even number.)
else:
    print("It is not even number.)
\n""")

b = eval(input("Enter any number: "))
if b % 2 == 0:
    print(f"{b} is a even number.")
else:
    print(f"{b} is not a even number")


print("""
If Elif Else : it used when we have more than 1 condition.
      
if [conditional expression]:
    [statement(s) to execute]
elif [conditional expression]:
    [statement(s) to execute]
else:
    [statement(s) to execute]
\n""")

c = eval(input("Enter any number: "))

if c % 2 == 0:
    print(f"{c} is a even number.")
elif c % 2 != 0:
    print(f"{c} is a odd number.")
else:
    print(f"{c} is not even number.")
