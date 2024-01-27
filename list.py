# Create a new list and their functionality with the help of ctype.
import ctypes

class List:
    def __init__(self):
        self.size = 1
        self.n = 0
        self.A=self.__make_array(self.size)
    
    def __make_array1(self,capacity):
        return (capacity*ctypes.py_object)()      
    
    # Creating len function
    def __len__(self):
        return self.n
    
    def append(self,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        
        self.A[self.n]= item
        self.n += 1
    
    def __resize(self,new_capacity):
        B=self.__make_array(new_capacity)
        self.size = new_capacity
        for i in range(self.n):
            B[i] = self.A[i]
        self.A=B 
        
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result+str(self.A[i])+','
        return '['+result[:-1]+']'
    
    def __getitem__(self,index):
        if 0<=index<self.n:
            return self.A[index]
        else:
            return 'Index error:Index out of range'
    
    def pop(self):
        if self.n==0:
            return "Empty list"
        
        print(self.A[self.n-1])
        self.n = self.n-1
    
    def clear(self):
        self.size = 1
        self.n = 0 
    
    def find(self,item):
        for i in range(self.n):
            if self.A[i]==item:
                return i
        return 'ValueError:Value not find'
        
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n = self.n + 1
        
        
    def __delitem__(self,pos):
    # delete pos wala item
        if 0<= pos < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n - 1
obj = List()
print(obj) 
obj.append('Neeraj')
obj.append('Raj')
obj.append('Jai')
obj.append('Rahul') 
print(len(obj))
print(obj)
print(obj.find("aj"))