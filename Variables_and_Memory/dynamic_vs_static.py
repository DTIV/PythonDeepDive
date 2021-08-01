# DYNAMIC VS STATIC TYPING

''' Python is dynamically typed - the variable can be whatever, it just changes the memory address for what is needed and rewrites.
Static typed must specify type and the variable is specific to that type always '''


print("Python variables can change dynamically throughout the code, changing variable memory addresses")

a = "hello"
print(type(a))
print(hex(id(a)),"\n")

a = 10
print(type(a))
print(hex(id(a)),"\n")

a = 10.23
print(type(a))
print(hex(id(a)),"\n")

a = True
print(type(a))
print(hex(id(a)),"\n")

a = lambda x: x ** 2
print(type(a))
print(hex(id(a)),"\n")

a = 3 + 4j
print(type(a))
print(hex(id(a)))