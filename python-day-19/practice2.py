import json
json_data = '{"Name": "Aarthi", "Age": 18, "City": "Chennai"}'
student_dict = json.loads(json_data)
print(student_dict["Name"])