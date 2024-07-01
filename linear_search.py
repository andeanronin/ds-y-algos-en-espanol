# Linear Search Algorithm:
# LinearSearch(array, key)
#    for each element in the array
#        if element == value
#            return its index

# Linear Search Program

def LinearSearch(array, k):
    for j in range(len(array)):
        if (array[j] == k):
            return j
    return -1

if __name__ == "__main__":
    # Searching value k in array:
    array = [1, 3, 5, 7, 9]
    k = 8
    result = LinearSearch(array, k)
    if(result == -1):
        print("Element not found")
    else:
        print("Element found at index: ", result)