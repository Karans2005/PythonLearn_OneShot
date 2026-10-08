# *args--
# Jab hume function me kitne bhi numbers/values bhejne ho, tab *args use kar sakte hain.

def add(*args):
    print(args)
add(10, 20, 30, 40)
# args ke andar values tuple ke form me aati hain.

# Example:
def add(*args):
    total = 0

    for number in args:
        total += number

    print(total)
add(10, 20, 30, 40)
# Simple meaning: *args = multiple positional values

# **kwargs
# kwargs ka use multiple key-value pairs bhejne ke liye hota hai.

def student(**kwargs):
    print(kwargs)
student(name="Harsh", age=21, city="Durg")
# Ye values dictionary ke form me aati hain.

# Ex--
def student(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student(name="Harsh", age=21, course="Python")
# Simple meaning: **kwargs = multiple key-value pairs

# lambda
# Lambda ek small one-line function hota hai.

# Normal function:
def square(x):
    return x * x
print(square(5))

# Lambda:
square = lambda x: x * x
print(square(5))
#  Syntax:  lambda arguments: expression

# Example:
add = lambda a, b: a + b
print(add(10, 20))

# map()
# map() ka use har value par ek function apply karne ke liye hota hai.

# Example:
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x * 2, numbers)
# print(tuple(result))
print(list(result))
# Simple meaning: map() = har item ko transform/change karo

# filter()
# filter() ka use condition ke according values select karne ke liye hota hai.

# Example:
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
# Simple meaning: filter() = condition ke according items chuno.

# reduce()
# reduce() ka use multiple values ko ek single result me combine karne ke liye hota hai.
# Iske liye functools se import karna padta hai: from functools import reduce.

from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, numbers)
print(result)
# Simple meaning: reduce() = multiple values → one final value. and ExPlore note.txt