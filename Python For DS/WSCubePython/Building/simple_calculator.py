print("""
+ ADD
- SUBSTRACT
* MULTIPLY
/ DIVIDE 
\n""")


value1 = eval(input("Enter a Value 1: "))
value2 = eval(input("Enter a Value 2: "))
operation = input("Enter operation:(+,-,*,/) ")
if operation == "+":
    print(value1+ value2)
elif operation == "-":
    print(value1-value2)
elif operation == "*":
    print(value1* value2)
elif operation == "/":
    print(value1/value2)
else:
    print("Enter Mentioned operation only")
