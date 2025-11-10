import datetime

a =datetime.datetime.now()
print(a)

print()

print(datetime.time())

print()

print(datetime.datetime(2000,2,17))

print()
x = datetime.datetime.now()
m = x.strftime("%I")
print(m)
