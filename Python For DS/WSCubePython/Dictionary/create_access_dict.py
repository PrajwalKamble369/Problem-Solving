print("Create Dictionary \n")
d = {
    "A":"a",
     "B":["Prajwal",1,1],
     3:[4,5,6],
     "sub":{"Lang":["Python","C","C++"]}
     }
print("Access elements from dictionary \n")
print("Accessing elements using keys:")
print(d["A"])

print("Accessing elements using for loop or itrting dictionary:")
for k in d:
    print("key:",k,"|","values:", d[k])

