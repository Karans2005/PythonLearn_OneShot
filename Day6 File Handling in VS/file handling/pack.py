# file = open("student.txt", "r")

# data = file.read()

# print(data)

# file.close()

# ///////////////////////////////////////////////////////////////////////////////

# Isse file apne aap ban jayegi aur usme text write ho jayega_

# with open("student.txt", "w") as file:
#     file.write("Name: Harsh\nCourse: B.Tech\nCollege: KEC")

# # Ab aap apni read wali lines chalayein_

# with open("student.txt", "r") as file:
#     data = file.read()
#     print(data)

# note: file is a variable w,r me Ji.

# //////////////////////////////////////////////////////////////////////////////////
# ReContinue

# file = open("student.txt", "w")

# file.write("Hello Harsh")

# file.close()

# file = open("student.txt", "a")

# file.write("\nPython")

# file.write("\nJava")
# file.close()

# file = open("student.txt", "w")

# file.write("\nPython")

# file.close()

# # File mein multiple lines likhna
# with open("student.txt", "w") as file:
#     file.write("Harsh\n")
#     file.write("Python\n")
#     file.write("Developer\n")

# readline()
# Sirf ek line read karni ho:

# with open("student.txt", "r") as file:
#     print(file.readline())

# readlines()
# Saari lines ko list ke form mein:

with open("student.txt", "r") as file:
    lines = file.readlines()

print(lines)