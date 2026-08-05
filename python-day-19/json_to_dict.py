import json
json_data = '{"Name": "Aarthi", "Age": 18, "Course": "CSE"}'
student_dict = json.loads(json_data)
print(student_dict["Name"])
print(student_dict["Course"])