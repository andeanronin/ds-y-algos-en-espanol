from array import *

# 1. Creating array of type 'i' , meaning intergers of two bytes 
array_integers = array('i', [10,20,30,40,50])

# 2. Traversing the array:
for x in array_integers:
    print(x)

# 3. Accessing an element in the array
print("")
print("item at index 2:")
print(array_integers[2])
print("")

# 4. Inserting an element in the array
array_integers.insert(1, 140) # inserts 140 at index 1
for x in array_integers:
    print(x)

# 5. Deleting an alement in an array
array_integers.remove(140)
print("")
for x in array_integers:
    print(x)
print("")
# 6. Searching in an Array
print("The index of 50 is: ")
print(array_integers.index(50))   # getting the index of array 50

# 7. Updating an Array
array_integers[2] = 300 # changes the value at index 2 from 30 to 300