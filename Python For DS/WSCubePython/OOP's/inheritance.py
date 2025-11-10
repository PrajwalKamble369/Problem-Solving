print('''
Inheritance :
      In inheritance there are more than 2 class are involved.
      Suppose we have 1st class "a" and 2nd class "b". And the we want to inherite all the properties of "a" to "b" , in this case we use inheritance concept.It is like parent and child.
      In this we dont need to create object for both(all) class. We have to create object of class which inhearant(child).

      There are 3 types of Inheritance:
        1) Single Inheritance      : oneclass(parent) => otherclass(child)
        2) Multi Level Inheritance : oneclass=> 2nd class => 3rd class
        3) Multiple Inheritance    : class a & class b => class c
\n''')

class A:
    def displayA(self):
        return "Welcome to Python A"

# single inheritance   
class B(A):
    def displayB(self):
        return "Welcome to Python B"
    
# multi-level inheritance
class C(B):
    def displayC(self):
        return "Welcome to Python C"
    
# multiple inheretance
class D:
    def displayD(self):
        return "Welcome to D"
    
class E:
    def displayE(self):
        return "Welcome to E"
    
class F:
    def displayF(self):
        return "Welcome to F"

class G(D,E,F):
    def displayG(self):
        return "Welcome to G"

    
obj = G()
print(obj.displayD())
print(obj.displayE())
print(obj.displayF())
print(obj.displayG())