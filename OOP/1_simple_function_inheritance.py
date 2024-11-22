class Parent(object):
    def function1(self):
        print("This function belongs to parent class")
        
class Child(Parent):
    def function2(self):
        print("This function belongs to child class")
     
# Create instance of Child class   
nico = Child()
nico.function1() # calling function 1 from Child class
nico.function2() # calling function 2 from child class