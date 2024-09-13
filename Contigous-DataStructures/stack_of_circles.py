
# import Stack class 
from stack_datastructure import Stack

# Create circle class:
class Circle(object):
    def __init__(self):
        self.radius = 0
    def __str__(self): # when user prints a Circle object it will tell them: 
        return f"Circle with a radius of {self.radius}" 
    def update_radius(self,radius):
        self.radius = radius 
    def get_radius(self):
        return self.radius 
    

# Create stack of circles object:
stack_of_circles = Stack()

# Create circles 
circle_one = Circle()
circle_two = Circle()
circle_three = Circle()

# Give radiuses to circles
circle_one.update_radius(4)
print(" First Circle Created:", circle_one)
print("")
circle_two.update_radius(2)
circle_three.update_radius(8)

# Add circles to stack of circles:
stack_of_circles.add_item(circle_one)
stack_of_circles.add_item(circle_two)
stack_of_circles.add_many(circle_three,4) # adds the circle three object 4 times (same object)

# Print stack of circles
print("Stack of circles:")
stack_of_circles.prettyprint()
