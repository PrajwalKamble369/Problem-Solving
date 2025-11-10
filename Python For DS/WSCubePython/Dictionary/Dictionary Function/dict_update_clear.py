print('''
dict()    : It is used to create a dictionary.
update()  : It used update values in dictionary.
clear()   : Clear the data from  and returns empty dictionary.
\n''')

print("dict('name'='Python','fees'=9000):")
d = dict(name= "Python", fees= 9000)
print(d)

print()

d.update({"fees":10000})
print("update({'fees':10000}):")
print(d)

print()

print("clear()")
d.clear()
print(d)

print()

print("Inserting New Keys and values")
d["description"] = "This is Python Programming Language"
d["Name"] = "Python"
d["expense"] = 1000
print(d)

print()

print("Updating Values of Dictionary:")
d["expense"] = 2000
print(d)

