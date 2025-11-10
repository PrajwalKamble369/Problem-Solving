print("""
User Input      : Getting Input From Casting
Type Casting    : Coverting input to suitable (required) datatype
      
Key Points:
            1) input()
            2) int()
            3) float()
            4) eval()
\n""")

user_input = int(input("Give Input :"))
user_input0 = int(input("Enter Input :"))
print(user_input+user_input0,"\n")

user_input1 = float(input("Enter Float Value :"))
user_input2 = float(input("Enter Float value"))
print(user_input1+user_input2,"\n")

user_input3 = eval(input("Enter Float or Integer :"))
user_input4 = eval(input("Enter Float or Integer :"))
print(user_input3+user_input4)

