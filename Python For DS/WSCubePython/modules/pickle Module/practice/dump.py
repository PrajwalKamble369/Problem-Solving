d ={
    "a":[10,20,30,40,50],
    "b":[100,200,300,400,500]
    }

import pickle
f = open("practice.txt","wb")
pickle.dump(d,f)
f.close()

pickle.dump(d,open("practice.txt","wb"))