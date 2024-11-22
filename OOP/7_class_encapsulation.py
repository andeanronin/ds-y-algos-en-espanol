 
# Python program to 
# demonstrate protected members 
  
# Creating a base class 
class Base: 
    def __init__(self): 
  
        # Protected variable 
        self._protected_variable = 2
  
# Creating a derived class 
class Derived(Base): 
    def __init__(self): 
  
        # Calling constructor of Base class:
        Base.__init__(self) 
        print("Calling protected member of base class: ",  self._protected_variable) 
  
        # Modify the protected variable: 
        self._protected_variable = 3
        print("Calling modified protected member outside class: ", self._protected_variable) 
  
print("")
derived_object = Derived()  # prints and modifies protected variable of parent class
base_object = Base()  # prints nothing

# Accesing the base's protected variable, which in theory should not be done due to convention 
print("")
print("Accessing protected variable of base_object from derived_object: ", derived_object._protected_variable) 

# Accessing the protected variable outside 
print("Accessing protected member of base_object directly: ", base_object._protected_variable) 