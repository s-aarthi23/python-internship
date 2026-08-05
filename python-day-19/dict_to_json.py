import json
student = {
    "Name":"Aarthi",
    "Age":18,
    "Couerse":"CSE"
}
json_data = json.dumps(student, indent=4)
print(json_data)