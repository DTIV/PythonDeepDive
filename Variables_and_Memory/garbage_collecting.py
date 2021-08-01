###     2. Garbage Collecting       ###

import ctypes
import gc

def object_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object Exists"
    return "Not Found"

def ref_count(address: int or None):
    try:
        return ctypes.c_long.from_address(address).value
    except:
        return None
        
'''
Create a circular memory reference and disable garbage collector
'''
class A:
    def __init__(self):
        self.b = B(self)
        print('A: self:', hex(id(self)),'self.b:', hex(id(self.b)))

class B:
    def __init__(self,a):
        self.a = a
        print('B: self:', hex(id(self)),'self.a:', hex(id(self.a)))

gc.disable()

print("Circular reference between classes:")
gc_vara = A()

a_id = id(gc_vara)
b_id = id(gc_vara.b)

print("\nReturn mem address of a through object instance of b")
print("A:",hex(a_id))
print("B:",hex(id(b_id)))
print("A.B.A:",hex(id(gc_vara.b.a)))

print("\nreference count for A:",ref_count(a_id))
print("\nreference count for B:",ref_count(b_id))

'''
Check if objects exist
'''
print("Checking if objects exist in garbage collector...")
object_by_id(a_id)
object_by_id(b_id)

'''
Destroy memory reference for object A, Check reference count
'''
print("destroying A..")
gc_vera = None

print("A reference count:",ref_count(gc_vara))
print("B reference count:",ref_count(b_id))

print("A object:", object_by_id(a_id))
print("B object:", object_by_id(b_id))

''' Collect Garbage manually'''
print("\nCollecting Garbage...")
gc.collect()

print("A object after:", object_by_id(a_id))
print("B object after:", object_by_id(b_id))

ref_count(a_id)
ref_count(b_id)