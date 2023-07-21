# Create a new list and their functionality with the help of ctype.
import ctypes

class List:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A=self.__make_array(self.size)
    
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()      
    
obj = List()
print(obj)  