Day 21 – Requests Library

📚 Topics Covered

What is an API?

What is the Requests library?

Sending a GET request

Understanding response

HTTP status codes

Using response.json()

Accessing specific data from JSON response


🧠 What I Learned

1. API

API (Application Programming Interface) helps different applications communicate with each other.

2. Requests Library

The requests library is used in Python to send HTTP requests to APIs and websites.

import requests

3. GET Request

response = requests.get("https://api.github.com")

A GET request is used to request information from an API.

4. Status Code

print(response.status_code)

200 means the request was successful.

5. JSON Response

data = response.json()

This converts the API response into Python data that can be used in our program.

6. Accessing Specific Data

print(data["current_user_url"])

This accesses a particular value from the JSON data.

💻 Practice Programs

Sent a GET request to the GitHub API.

Checked whether the request was successful using status_code.

Retrieved JSON data from the API.

Accessed a specific value from the JSON response.


🎯 Conclusion

Today I learned the basics of working with APIs using Python's Requests library. I practiced sending GET requests, checking status codes, reading JSON responses, and accessing specific data.

Day 21 Completed ✅ 🐍
