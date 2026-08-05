import json
data = {
    "Name": "Aarthi",
    "Age": 18,
    "City": "Chennai"
}
json_data = json.dumps(data, indent=4)
print(json_data)