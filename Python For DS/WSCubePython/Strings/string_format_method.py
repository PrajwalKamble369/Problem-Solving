print('''
String Format Method :
      When we have use a perticular value at runtime then we use format() method.
\n''')

print("My name is {0} {1}".format("Prajwal","Kamble"),"\n")

print("My name is {} {} and I studying {} for {} {}.".format("Prajwal","Kamble","Python","Data","Science"),"\n")

print("Hello {1} {0}".format("Rahul",101)) # Rahul {0} and 101{1}

w = "welcome to {a:^10} {b}.".format(a="Python", b ="Learning")
print(w)

a = "Prajwal {}"
print(a.format("Kamble"))

templet = "Hello my {} is {} {} and how are you buddy"
name = "name"
na = "Prajwal"
lana = "Kamble"
print(templet.format(name,na,lana))
