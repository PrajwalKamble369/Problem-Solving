print('''
Encapsulation :
      Encapsulation in Python is the practice of restricting direct access to an object's data by using private variables and providing access to method.
      
      Getter : Get the value

      Setter : Set the value
\n''')

class Student:
    def __init__(self,name,marks):
        # public variable
        self.name= name
        # private variable (encapsulation)
        self.__marks = marks
        
    # accessing method
    def get_marks(self):
        return self.__marks
    
    # setting method
    def set_marks(self,marks):
        self.__marks = marks
   
obj = Student("Prajwal",50)
obj.set_marks(90)
print(obj.get_marks())


# practice 
# we need getter and setter method
class EncapsulationPracticle:
    def __init__(self,name,age,income,education):
        self.name = name
        self.__age = age
        self.__income = income
        self.education = education

    # getter for age
    def get_age(self):
        return self.__age
    
    # getter for income
    def get_income(self):
        return self.__income
    
    # setter for age
    def set_age(self,age):
        self.__age = age

    # setter for income
    def set_income(self,income):
        self.__income = income

    
obj0 = EncapsulationPracticle("Prajwal",25,45000000,"btech")

print(obj0.get_age())