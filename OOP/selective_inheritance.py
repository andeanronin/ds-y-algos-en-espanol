

class Parent():
    def __init__(self, name, age, profession=None):
        self.name = name
        self.age = age
        self.profession = profession
        
    def introduction(self):
        print(f"My name is {self.name}, I am {self.age} years old.")

class Child(Parent):
    # add own instance attributes: school & grade
    def __init__(self, name, age, school, grade):
        self.school = school
        self.grade = grade
        
        # invoke Parent's class name and age attributes 
        Parent.__init__(self, name, age) # profession not included
        
    # create Class-specific function:
    def student_intro(self):
        print(f"I go to {self.school} school and I am in grade {self.grade}.")


if __name__ == "__main__":
    print("")
    # Create Parent Object:
    juanfer = Parent('Juan Fernando', 65, 'Manager')
    juanfer.introduction()
    print("")

    # Create Child Object: 
    nico = Child('nico',24,'roosevelt',10)
    nico.introduction()                     # the nico object uses function from parent class
    nico.student_intro()                    # the nico objects call function of its own class 
    print("")