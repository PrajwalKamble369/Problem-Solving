print("""
Bitwise operator works on principle of bit values.
0 is considered as False.
1 is considered as True.

_____________________________________________________
| Operator  | Name     |        Description         |
|   &       | AND      |          x & y             |
|   |       | OR       |          x | y             |
|   ^       | XOR      |          x ^ y             |
|___________|__________|____________________________|


Truth Table :

    1 = True     0 = False
_____________________________________
| A   |  B  |  A&B  |  A|B  |  A^B  |
| 0   |  0  |   0   |   0   |   0   |
| 0   |  1  |   0   |   1   |   1   |
| 1   |  0  |   0   |   1   |   1   |
| 1   |  1  |   1   |   1   |   0   |
|_____|_____|_______|_______|_______|


for 
  & if both side have 1 then it is 1

for
  | if one side have 1 or both side have 1 then it is 1

for
  ^ if one side have 1 it then it is 1

\n"""
 )

x = 10
y = 8

x_bin = bin(x)
y_bin = bin(y)

print("& Operator :",x & y,"Binary of x and y:",x_bin, y_bin,"\n")

print("| (or) Operator:", x|y,"Binary of x and y:",x_bin,y_bin,"\n")

print("^ (XOR) Operator:", x^y,"Binary of x and y:",x_bin,y_bin,"\n")