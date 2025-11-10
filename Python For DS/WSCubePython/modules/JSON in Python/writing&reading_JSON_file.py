print("Reading Data")

import json
file = open("posts.json","r")
x = file.read()
final_data = json.loads(x)
print(final_data)