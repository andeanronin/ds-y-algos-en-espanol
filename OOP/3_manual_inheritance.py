class Parent():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduction(self):
        print(f"My name is {self.name}, I am {self.age} years old.")


class Child(Parent):
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        
        # invoke Parent's class name and age instance variables to inherit them 
        Parent.__init__(self, name, age) 
        
    def student_intro(self):
        print(f"I go to {self.school} school and I am in grade {self.grade}.")



# Create instance of Child class   
nico = Child('nico',24,'roosevelt',10)
nico.introduction() # the nico object uses function from parent class
nico.student_intro()        # the nico objects call function of its own class