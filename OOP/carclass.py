class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage 
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"
    

bluetoyota = Car("blue", 20000)

print(bluetoyota)

redtoyota = Car("red", 1000)

print(redtoyota)