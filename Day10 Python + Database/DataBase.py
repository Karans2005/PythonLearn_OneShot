# First explore note.txt and start coding .

# SQLite kya hai?
# SQLite ek lightweight database hai. import sqlite3

# Database se connect karna.

# import sqlite3
# connection = sqlite3.connect("students.db")
# print("Database connected")
#Note: Agar students.db exist nahi karti, SQLite automatically bana dega.

# Cursor banana
# Database ke saath SQL commands execute karne ke liye cursor use karte hain.

import sqlite3
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
# Ab hum: cursor se.
# se SQL commands chala sakte hain.

# Table create karna
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")
# Phir:
connection.commit()

# commit() kya karta hai?
# Database me jo changes kiye hain unko save karta hai.

# Data Insert karna
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Harsh", 21)
)
connection.commit() #Ab database me: student.db

# Multiple data insert
students = [
    ("Rahul", 22),
    ("Aman", 20),
    ("Rohit", 23)
]

cursor.executemany(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    students
)
connection.commit()
# executemany() ek saath multiple records insert kar sakta hai.

# Data Read karna
# Ab database se data nikalte hain.

# cursor.execute("SELECT * FROM students")
# students = cursor.fetchall()
# print(students)

# Specific data
cursor.execute("SELECT name, age FROM students")

students = cursor.fetchall()
for student in students:
    print(student)

# fetchone()
# Sirf ek record chahiye:

# cursor.execute("SELECT name, age FROM students")
cursor.execute("SELECT * FROM students")
student = cursor.fetchone()
print(student)

# Update
# Maan lo Harsh ki age 22 karni hai:

cursor.execute(
    "UPDATE students SET age = ? WHERE name = ?",
    (23, "Harsh")
)
connection.commit()
#Syntax: UPDATE table_name SET column_to_change = value WHERE condition_column = value

# Delete
# Harsh ka record delete:

cursor.execute(
    "DELETE FROM students WHERE name = ?",
    ("Harsh",)
)
connection.commit()
# Record delete ho jayega. and explore note.txt .

# CRUD =
# C → Create
# R → Read
# U → Update
# D → Delete

# Complete Example-***********
# Ek simple student database:

import sqlite3

# Connection
connection = sqlite3.connect("students.db")
# connection = sqlite3.connect("students2.db")


# Cursor
cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

# Insert
cursor.execute(
    "INSERT INTO students (name, age) VALUES (?, ?)",
    ("Harsh", 21)
)

connection.commit()

# Read
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

# Close
connection.close()