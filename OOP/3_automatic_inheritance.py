# This file creates two classes: a Parent and  Child Class
# The child class inherits the Parent's instance attributes (name, age) and its methods

# Create Parent Class:
class Father(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_attributes(self):
        print('Name: ', self.name)
        print('Age: ', self.age)


# Create Child Class       
class Child(Father):
    # Child class has no __init__ method --> thereby inherits parent class's instance variables automatically

    def child_introduction(self):
        print(f"I am a child my name is {self.name} and I am {self.age} years old. ")


if __name__ == "__main__":
    print("")
    nicofather = Father('Miguel', 65)     # Create Father Object named nicofather
    nicofather.display_attributes()     # Run Father class Method display_attributes()
    print("")

    # Create Child Object named nico    
    nico = Child('Angel',24)   # give it inherited instance variables: name, age
    nico.display_attributes() # use parent method display_attributes()
    nico.child_introduction()        # uses own method  child_intro()
    print("")