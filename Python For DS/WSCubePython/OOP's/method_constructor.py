print('''
Method & Constructors:
    Methods :
      Method is function inside classs and written with self keyword. It get called when object is called.
      
    Constructor :
      Constructor is also a method but it we dont need to call it by calling object. When we created an object the constructor get called or trigger at time not need to run object.

      Note : The main difference between constructor and method is we doest not need to call constructor but we need to call method.
\n''')

print("Methods: \n")

class DemoClass:
    a = 10
    def showvalue(self):
        # a is variable and not argument of this method so self is required
        self.c = self.a*self.a
        return self.c

    def showvalue1(self,a,b):
        # a and b are argument of this method so self is not required
        return a+b

obj = DemoClass()
print(obj.showvalue())
print(obj.showvalue1(1,2),"\n")

print("Creating Constructor: \n")

class DemoClass1:
    a = 10
    def __init__(self):
        print("Hi Prajwal")
    def method1(self):
        return "Hello"
    
a = DemoClass1()
print(a)
print(obj)
