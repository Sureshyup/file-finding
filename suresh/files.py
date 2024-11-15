import json
data={"name":"suresh","age":"20"}
with open("data.json","w")as file:
    json.dump(data,file)

with open("data.json","r")as file:
    data=json.load(file)
    print(data)
