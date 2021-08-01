
'''
this is my follow through of the Python Deep Dive course by Fred Baptiste on Udemy
hands down the best python course on udemy by far 
'''


###     1. Variables and Reference Counting    ###

import sys
import ctypes

'''
Variables are references to memory addresses
 -find out the memory address of a variable using id()
 -id() returns a base-10 number
 -convert the base-10 to a hexidecimal using hex()

'''
a = [1,2,3]

print("variable memory address in base-10 and hexidecimal:")
print("base-10:", id(a))
print("hexidecimal:",hex(id(a)),"\n")


'''
Two variables can reference the same memory address
'''
new_var = a
print("two variables referencing the same memory address:")
print(id(new_var))
print(id(a),"\n")

'''
Get the count of references at a memory address using getrefcount
 -getrefcount adds another reference count to the memory address
 -ctypes does not add another reference count
'''

def ref_count(address: int or None):
    try:
        return ctypes.c_long.from_address(address).value
    except:
        return None

print("getrefcount() adding another reference count:",sys.getrefcount(a))
print('true reference count using ctypes:',ref_count(id(a)),"\n")
