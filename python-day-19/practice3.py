import json
data = {
    "Name": "Aarthi",
    "Age": 18,
    "City": "Chennai"   
}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    new_data = json.load(file)

print(new_data)