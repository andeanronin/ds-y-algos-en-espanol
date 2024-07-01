
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
print("")

# Create objects of both classes
obj_ind = India()
obj_usa = USA()

# Function uses two different class types (India & USA) in the same way. 
for country in (obj_ind, obj_usa):
    country.capital()     # Python calls the same method on both classes
    country.language()    # no concern on which class the method belongs to
    country.type()
print("")