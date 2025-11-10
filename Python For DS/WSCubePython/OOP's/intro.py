print('''
Object Oriented Programming(OOP's):
      (Class, Object)

      Class :
        Class is a blueprint of object in which we can define methods, variable.
      
      Object :
        To call the functions (methods) of class we created an object or objects. 
\n''')

print("Creating Class and creating Object of class: ","\n")

# creating class
class DemoClass:
    # creating variable
    a = 10
    # defining method
    def hello(self):
        return "Hello Buddy"

ob = DemoClass()
print(ob.hello())

# self is work itself as an object
   
