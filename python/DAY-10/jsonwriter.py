import json

data = {
    "NAME": "Jocima",
    "ROLL_NO": "20",
    "DEPARTMENT": "AI&DS"
}
with open("DAY-10/jsondata.json","w") as file:
    json.dump(data,file,indent=4)