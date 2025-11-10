print('''
Converting JSON to Python Objects:
      If you have JSON string, you can parse it by using the json.loads() method.

    Syntax :
      # some JSON
      x = '{"cname":"python","fees":1200,"duration":"2 Months"}'

      # parse x
      y = json.loads(x)

      # the result is python dictionary
\n''')

import json
d = {
    "course_name":"python",
    "duration":"2 Months",
    "fees": 0,
    "dificulty":"Easy"
    }
# converting dict to JSON Object
j_ob = json.dumps(d)
print("Python Object to JSON Object: ",j_ob,"\n")
# converting JSON Object to Python Object
py_ob = json.loads(j_ob)
print("JSON Object toPython Object: ",py_ob,"\n")
print(type(py_ob))