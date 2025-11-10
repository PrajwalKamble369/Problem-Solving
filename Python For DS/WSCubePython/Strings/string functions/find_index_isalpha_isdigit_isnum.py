print('''
Python String Functions:
      1) find()    : It is used find index number of character from string.
      2) index()   : It is similar to find.
      3) isalpha() : It gives value is true and false. It checks are the alphabets used in string.
      4) isdigit() : It gives value is true and false. It checks are the all characters in string are numbers.
      5) isalnum()   :It gives value is true and false. It is checks in string contain number or characters. 
\n''')

string = "Prajwal Kamble Data Scientiest"

print("it retuns result when first character is get or find out|","index number of 'al':",string.find("al"),"\n")
print(string.find("a",3),"\n")
print("if the value is not found it give result in -1:", string.find("z"),"\n")

print(string.index("e"),"It give error if value is not present in string thats the difference between find() and index()\n")

print(string.isalpha())

print(string.isdigit())

print(string.isalnum())