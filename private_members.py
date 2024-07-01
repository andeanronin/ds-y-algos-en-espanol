
# Python program to demonstrate private members 
  
# Creating a Base class 
  
class Base: 
    def __init__(self): 
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c)  # raises error
  
  
# Driver code 
obj1 = Base() 
print(obj1.a) 
print(obj1.__c)  # Raises Attribution error: Base has no attribute __c

obj2 = Derived()   # Raises Attribution Error --> private member of base class is called inside derived class
