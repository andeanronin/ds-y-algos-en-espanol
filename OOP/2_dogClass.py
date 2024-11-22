class Dog:
    bark = print('BARK BARK BARK') # this is a class variable, given that all dogs bar --> therefore this class variable (bark) is shared by all dog instances of class dog

    def __init__(self, name, race, color): # instance variables are variables that will be unique for each instance of the class --> each dog will have a unique instance variable such as name, race etc 
        self.name = name
        self.race = race
        self.color = color
        self.tricks = []   # creates an empty list for every dog created, stored in instance variable tricks

    def add_trick(self, trick):
        self.tricks.append(trick)
    
myPuppy = Dog("terminator", "labrador", "black")

myPuppy.bark

print(myPuppy.name)
print(myPuppy.race)

myPuppy.tricks.append('jump')
myPuppy.tricks.append('fetch')

print(myPuppy.tricks)