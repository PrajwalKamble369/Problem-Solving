print('''
Nested Dictionary:
      It means dictionary inside a dictionary.
      It is used to collect all data together.
\n''')

course = {
        "python":{"duration":"2 Months", "fees":3000},
        "ML":{"duration":"3 Months","fees":4000},
        "DL": {"duration":"1 Month","fees":1000},
        "NLP": {"duration":"15 Days", "fees":2000}
        }

print(course)

print()

course["python"]["duration"] = "20 Days"
print(course)

print()

print("Duration for Python : ",course["python"]["duration"])

print()

for k ,v in course.items():
    print("Keys:",k,"|","values:",v)

print()

for k ,v in course.items():
    print("Keys:",k,"|","values:","|","duration:",v["duration"],"|","fees:",v["fees"])