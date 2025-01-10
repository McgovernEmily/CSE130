data_names = {
    "name" : "Emily",
    "age" : "two",
    "numbers" : ["one", "two", "three"],
    "year" :1991
}

import json

text = json.dumps(data_names)
with open("data_names.json", "w") as file:
    file.write(text)

with open("data_names.json", "r") as file:
    text2 = file.read()
    data2 = json.loads(text2)

print(data2)
#json file to dictionary and readable