a = 10
b = 10

print("a:",a,"b:",b,"\n")

print("Memory address of a",id(a),"Memory address of b",id(b),"\n")

print(id(a)==id(b),"| If the output is true then the memory address is same \n")

print("hence it is proved that memory location in python is based on value of variable not on variable name")

# now create two variables named as c and d with different values

c = 12
d = 15
print("Memory address if c:",id(c),"Memory address of d:", id(d),"\n")

print(c==d, "| if it is false then the memory address is differnt for these two variables and it is located based on the values of variable")