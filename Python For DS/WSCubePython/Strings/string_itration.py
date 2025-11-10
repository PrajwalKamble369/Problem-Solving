print('''
String Itration :
            1) We used for Loop
''')

s = "Welcome to Python Learning Journy"
s_r = s[-1::-1]
s_len = len(s)
print(s_len,"\n")

for  i in range(s_len):
    print(s[i],end=" ")
    print(s_r[i],end=" ")

for i in range(s_len-1,-1,-1):
    print(s[i])

for i in s:
    print(i)

for i in s:
    print(i)
print("")