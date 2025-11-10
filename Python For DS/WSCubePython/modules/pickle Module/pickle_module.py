print('''
It is used to store python data in file.
      The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a python object structure.

      serializing      : means store data.

      de-serializing   : means read data.


    You can pickle objects with following data types:
      1) Booleans
      2) Integers
      3) Floats
      4) Complex Numbers
      5) (Normal and Unicode) Strings
      6) Tuples
      7) Lists
      8) Sets
      9) Dictionaries

Pickle has two main methods. The first one is dump, which dumps an object and the second one is load, which loads an objects from a file object.      

      dump() - This function is called to serialize an object hierarchy.

      load() - This function is called to de-serialize a data stream.

      Pickling with dump() :
        Pickling data is done via dump function. It accepts data and file object. 
        The dump() function then serializes the data and weites it to the file .

        Syntax of dump() :
           import pickle
           example = {"a":[1,2,3],"b":[10,20,30]}
           pickle_write = open("text.text","wb")
           pickle.dump(example, pickle_write)
           pickle_write.close()
      
      _______________________________________________________
      | Argument   | Description                            |
      | obj        | Object to be picked                    |
      | file       | file object where data will br written |
      |____________|________________________________________|

        Syntax of load() :
         import pickle
         f = open("text.txt","rb")
         pickle.load(f)
\n''')

print("dump() :\n")
import pickle
l = [10,20,30,40,60]

file = open("writedata.txt","wb")
pickle.dump(l,file)
file.close()