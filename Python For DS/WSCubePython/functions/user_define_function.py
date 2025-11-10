print('''
User Define Function:
      These are used for the perticular use and can be reused.
    1) Simple Function :
      # defining function
      def simple_function():
          print("Welcome to Python learning Journy !")
      # calling function
      simple_function()
          
      
    2) Function with arguments :
      # defining function with arguments
      def func_with_argu(a,b):
          print(a+b)
      # calling function
      func_with_argu(4,5)

      Note: we can also set default value in argument
      def default_value(a=5,b):
            print(a+5)
      default_value(2)

      # function with arbitary position arguments (it is positional argument and store values as tuple)
      def arb_pos_argu(*args):
            print(args)
      # calling function
      arb_pos_arhu(1,2)

      # keyword argument store the values as dictionary
      def kwargu(**kwargs):
            print(kwargs)
      kwargu(name=="Prajwal,age=25)


    3) Return Type Function :
      def return_funct(a,b):
            c = a +b
            return c
''')

print("Positional argument:")
def func(*a):
    return a

print(func(1,2),"\n")


print("Keyword Argument:")
def k_func(**ka):
    return ka

print(k_func(name= "Prajwal",surname= "Kamble",age=25),"\n")

print("Simple Function:")
def nor_func():
    print("Hello")

print(nor_func(),"\n")

print("Function with arguments:")
def funct_with_argu(a,b):
    print(a+b)

print(funct_with_argu(1,2),"\n")

print("Function with return:")
def funct_return(a,b):
    return a+b

print(funct_return(1,2),"\n")
