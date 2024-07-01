# Base class1
class Mother:
    mothername = ""
    
    def mother(self):
        print(self.mothername)
 
 
# Base class2
class Father:
    fathername = ""
 
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father): # inherits 2 classes
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
if __name__ == "__main__":
    print("")
    s1 = Son()
    s1.fathername = "RAM"    # Calls fathername attribute and sets it to "RAM"
    s1.mothername = "SITA"
    s1.parents()