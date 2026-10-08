# 🐍 Python One-Shot Learning

Welcome to my **Python One-Shot Learning Repository** 🚀

This repository contains my complete **10-Day Python Learning Journey**, starting from the basics and progressing to **OOPs, File Handling, APIs, JSON, and Database Connectivity**.

The goal of this repository is to learn Python concepts in a simple and structured way and maintain all my learning code in one place.

---

## 📚 10-Day Python Learning Roadmap

### 🟢 Day 1 — Basic Python

Learned the fundamentals of Python:

- Python Introduction
- Variables
- Data Types
- Input & Output
- Operators
- Conditional Statements
- `if`, `elif`, `else`
- Loops
- `for` Loop
- `while` Loop
- `break`
- `continue`
- Lists
- Tuples
- Sets
- Dictionaries

---

### 🟢 Day 2 — Functions

Learned how to create and use functions:

- What is a Function?
- `def`
- Function Calling
- Parameters
- Arguments
- Return Statement
- Default Arguments
- Multiple Parameters
- Local & Global Variables

Example:
```python
def greet():
    print("Hello Python")

greet()
```

---

### 🟢 Day 3 — Strings

Learned Python String concepts:

- String Creation
- String Indexing
- String Slicing
- String Methods
- `upper()`
- `lower()`
- `strip()`
- `replace()`
- `split()`
- `join()`
- String Formatting
- f-Strings

Example:
```python
name = "Harsh"

print(name.upper())
print(f"Hello {name}")
```

---

### 🟢 Day 4 — OOPs

Learned **Object-Oriented Programming in Python**:

- Class
- Object
- `__init__()`
- `self`
- Methods
- Constructor
- Inheritance
- Encapsulation
- Polymorphism

Example:
```python
class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)


student = Student("Harsh")
student.show()
```

---

### 🟢 Day 5 — Modules & Packages

Learned how Python code can be organized into reusable modules and packages:

- Modules
- `import`
- `from ... import`
- Built-in Modules
- Creating Own Modules
- Packages
- `__init__.py`

Example:
```python
import math

print(math.sqrt(25))
```

---

### 🟢 Day 6 — File Handling

Learned how to work with files using Python and VS Code:

- Open Files
- Read Files
- Write Files
- Append Files
- `with open()`
- File Modes
- `r`
- `w`
- `a`

Example:
```python
with open("data.txt", "w") as file:
    file.write("Hello Python")
```

---

### 🟢 Day 7 — Error Handling

Learned how to handle errors and exceptions:

- `try`
- `except`
- `else`
- `finally`
- Common Exceptions
- Custom Errors
- Exception Handling

Example:
```python
try:
    number = int(input("Enter number: "))
    print(number)
except ValueError:
    print("Please enter a valid number")
```

---

### 🟢 Day 8 — Advanced Functions

Learned advanced Python function concepts:

- `*args`
- `**kwargs`
- Lambda Functions
- `map()`
- `filter()`
- `reduce()`
- Higher-Order Functions

Example:
```python
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)
```

---

### 🟢 Day 9 — APIs + JSON

Learned how Python communicates with APIs and works with JSON data:

- What is an API?
- HTTP Requests
- GET Request
- POST Request
- `requests`
- JSON
- JSON Parsing
- API Response Handling

Example:
```python
import requests

response = requests.get("https://api.example.com/data")

data = response.json()

print(data)
```

---

### 🟢 Day 10 — Python + Database

Learned how Python works with databases:

- Database Introduction
- SQLite
- Database Connection
- Create Table
- Insert Data
- Read Data
- Update Data
- Delete Data
- CRUD Operations
- Python Database Connectivity

Example:
```python
import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

connection.commit()
connection.close()
```

---

## 🛠️ Technologies Used

- 🐍 Python
- 💻 VS Code
- 🗄️ SQLite
- 🌐 REST APIs
- 📦 JSON
- 🔧 Git & GitHub

-------
