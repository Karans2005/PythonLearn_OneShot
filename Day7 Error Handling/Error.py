# Error kya hota hai?
# Jab program run karte waqt koi problem aati hai, usse Error/Exception kehte hain.

# Example:
# print(10 / 0)

# Error Handling ka use program ko safely handle karne ke liye hota hai.

# Try + Except

# Ex-
# try:
#     number = int(input("Enter number: "))
#     print(number)
# except:
#     print("Invalid input")

# note:
# Agar user:
# 10
# dale → normally chalega.
# Agar:
# abc
# dale → program crash nahi hoga, balki:
# Invalid input
# dikhega.

# Simple:
# try → risky code
# except → error aaye to ye code chalega

# Specific Error
# Better practice hai specific error batana:

# try:
#     number = int(input("Enter number: "))
# except ValueError:                        #number daloge to thik agr ni daloge ya a to z kuch bhi dal diye to exept wala chalega
#     print("Please enter a valid number")
# # ValueError tab aayega jab string ko number mein convert nahi kar paoge.

# Else
# else tab chalega jab koi error nahi aaya.

# try:
#     number = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number")
# else:
#     print("Your number is:", number)

# Finally 
# finally har situation mein chalega—error aaye ya na aaye.

# try:
#     number = int(input("Enter number: "))
# except ValueError:
#     print("Invalid number")
# finally:
#     print("Program finished")

# Sabko ek saath dekho*******************
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter numbers only")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")

# Yahan:
# try       → code try karo
# except    → error handle karo
# else      → error nahi aaya to chalao
# finally   → hamesha chalao    

# Custom Error :
# Kabhi-kabhi hum khud error raise karna chahte hain.
# Uske liye raise use karte hain.

age = 15
if age < 18:
    raise ValueError("Age must be 18 or above")
# Matlab humne khud condition ke according error generate kiya.

# Ekdum Short Mein
# try
#  ↓
# Risky code

# except
#  ↓
# Error handle

# else
#  ↓
# No error → ye chalega

# finally
#  ↓
# Har situation mein chalega

# raise
#  ↓
# Khud error generate karna

# Example yaad rakho:
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("0 se divide nahi kar sakte")
# finally:
#     print("Done")
