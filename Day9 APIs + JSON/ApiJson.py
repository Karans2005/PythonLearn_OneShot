# First ExPlore note.txt and then start coding.

# Python me JSON***
# Python me json module built-in hota hai.Ex_import json

# Python Dictionary → JSON***
# import json
# student = {
#     "name": "Harsh",
#     "age": 21
# }

# data = json.dumps(student)
# print(data)
# dumps() ka matlab: Python object → JSON string

# JSON → Python Dictionary***
import json

data = '{"name": "Harsh", "age": 21}'

student = json.loads(data)

print(student)
print(student["name"])
print(student["age"])
# loads(): JSON string → Python object.

# Yaad rakho:
# dumps() → Python → JSON
# loads() → JSON → Python

# requests module***
# API call karne ke liye Python me commonly: and explore note.txt .

# Demo
# import requests

# response = requests.get("https://jsonplaceholder.typicode.com/users")
# print("Response:",response.status_code)
# print("Result:",response.json())
# //////////////////////////////////////////////////////
# Yaha:
# requests.get()

# API ko request bhej raha hai.

# status_code
# print(response.status_code)

# Common status codes:
# 200 → Success ✅
# 201 → Created
# 400 → Bad Request
# 401 → Unauthorized
# 404 → Not Found
# 500 → Server Error

# API ka JSON data
# Agar API se data JSON me aaya:

# data = response.json()
# print(data)
# Ab tum us data ko Python list/dictionary ki tarah use kar sakte ho.

# Example:
# for user in data:
#     print(user["name"])

# Real checking****

import requests

# API Response ko JSON list me liya (manta hu aapne Result variable banaya hai)
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

print("--- ALL USERS LIST ---")
# Har user dictionary me se specific fields nikalna
for user in data:
    name = user['name']
    email = user['email']
    city = user['address']['city']
    
    print(f"👤 Name: {name} | ✉️ Email: {email} | 🏙️ City: {city}")

# why user['address']['city'] ?
# Yeh isliye aaya kyunki aapka JSON data Nested (Data ke andar Data) structure me hai.
# 'address': {
#       'street': 'Kulas Light', 
#       'city': 'Gwenborough', 
#       'zipcode': '92998-3874'
#   }

# Specific data nikalna***
# import requests

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/users"
# )

# data = response.json()

# print(data[0]["name"])
# print(data[1]["name"])
# print(data[2]["name"])

# POST Request
# POST ka use generally data server ko bhejne/create karne ke liye hota hai.

import requests

data = {
    "name": "Harsh",
    "age": 21,
    "city": "Durg"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=data
)

print("Response:",response.status_code)
print("Result:",response.json())
# json=data: server ko JSON data bhej raha hai. and EXplor note.txt

import requests

response = requests.get("https://job-backend-2bfw.onrender.com/jobs")

jobs = response.json()

print(jobs)