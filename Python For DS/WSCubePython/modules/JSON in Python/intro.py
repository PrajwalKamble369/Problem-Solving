print('''
JSON (Java Script Object Notation.)
It is mainly used for storing and transfering data between the browser and server.
JSON is text, written with java script object notation.
Python too support JSON with built-in package called json. 
      
JSON supports mainly 6 data types :
      1) String
      2) Numbers
      3) Booleans
      4) null
      5) Object
      6) Array

      In Python JSON exists as a string. For example: 
        p = '{"name":"Prajwal","lan":["Python","C","C++"]}'
\n''')

print("Converting a dictionary to JSON: \n")

import json

d = {
    "URL":"https://www.linkedin.com/feed/",
    "name":"Prajwal"
    }

f = json.dumps(d)
print("Data Type: ",type(f),"\n")
print(f)
