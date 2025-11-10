print('''
Polymorphism :
     There are two things in polymorphism Overloading & Overriding. 
      
    We can understand this in simple way, there is function called len in python it can calculate the length of string, list. So polymorphism say that even you provide list or string it calculates length, basically it is ability of function to behave with different data types.
      
    Polymorphism means same function name (but diiferent signature(behaviour with respect to data types)) being uses for different type. Means len function is used for calculating the length of the string aswell as list.
      
    In exact words ploymorphism is a abilty of function(method), object to behave differently based on data type or class of input it receives or based on how it is implemented in derived class.
\n''')

l = [10,20,30,40]
print("len for list:",len(l))

s = "welcome"
print("len for string:",len(s),"\n")


print("simple ploymorphism function(example):")
def add(x,y):
    return x +y

print("add for string:",add("a","b"))
print("add for numbers:", add(1,2),"\n")

print('''
Function Overloading (Overloading):
      It means the same method(function) behave differently for differnet argument.

Function Overriding (Overriding):
      Method overriding means a child class changes the way function works that it got from its parent class. This lets do things child class differently usning the same function name.(it simply override parent method to child method)
\n''')

print("Function Overloading(Overloading):")
class Pr:
    def displayinfo(self,name=""):
        if isinstance(name,int):
            return f"Welcome to python Joureny {name}"
        elif isinstance(name,str):
            return f"Welcome to python Journey {name}"
        else:
            return "Invalid Input"

ob = Pr()
print("using nothing as parameter as we set it already:",ob.displayinfo())

print("using string as parameter:",ob.displayinfo("Prajwal"))

print("using number as parameter:",ob.displayinfo(1),"\n")

print("Function Overriding (Overriding):")
class Animal:
    def sound(self):
        return "Animal makes sound"

class Dog(Animal):
    def sound(self):
        return "Dog barks"
    
a = Animal()
d = Dog()

print("sound metod of animal class (parent class):",a.sound())
print("sound method(inherited) of dog class(child):",d.sound(),"\n")

print("Using Super function to call the same name method in child claas. It enable extra functinality like parent can speak also child can speak with extra confidence. :")

class Animals:
    def sound(self):
        return "Animals Makes Sounds !"
    
class Cat(Animals):
    def sound(self):
        parent_sound = super().sound()
        return parent_sound + "but cat meow "
    
a0 = Animals()
c = Cat()
print("Sound in animals function:",a0.sound())
print("Sound in cat function:",c.sound(),"\n")

print("Abstract (Hinding unnecessary internal details and showing what is relevent to user):")
from abc import ABC, abstractmethod
class Vehical(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehical):
    def start(self):
        return "Car engine start"
    
c = Car()
print(c.start())