print(
"""
When we have to verify for more than one condition in this case we use "Logical Operators"
\n""")

print(
"""
____________________________________________________________________________________________
|  Operator  |          Description                                 |       Example        |
|   and      |Returns True if both conditions are true              |    x < 5 and x < 10  |
|   or       |Returns True if one of the statement is true          |    x < 5 or  x < 4   |
|   not      |Reverse the result, return False if the result is True|    not(x<5 and x<10) |
|____________|______________________________________________________|______________________|
\n""")

# declaring variable
x = 10

# and operator
print("And Operator(and)", x>10 and x==10,"\n")

# or operator
print("Or Operator(or)",x>10 or x==10, "\n")

# not operator
print("Not Operator (not)",not(x>10 and x==10))