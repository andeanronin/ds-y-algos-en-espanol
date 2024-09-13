
# Selection Sort Algorithm

def findSmallest(arr): 
    """
    Function that finds the smallest value in an array. 
    Input: array
    Output: smallest value
    Method: starts at index 0 and compares each next item
            Stores smallest item in variable "smallest"
    """
    smallest = arr[0] 
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest: 
            smallest = arr[i] 
            smallest_index = i
    return smallest_index


def selectionSort(arr): 
    """
    Function that sorts an array from smallest to largest
    Input: array
    Output: sorted array from smallest to largest 
    Method: iterates through array, gets smallest item and stores it in a "Sorted Array"
            iterates through array again, gets smallest item and stores it in the "Sorted Array"
            Repeats until there is no values in original array and all are in Sorted Array
    """
    sortedArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr) 
        sortedArr.append(arr.pop(smallest)) 
    return sortedArr
