import pickle
f = open("practice.txt","rb")
a = pickle.load(f)
print(a)