# Quicksort Algorithm for sorting an array

def quicksort(array): 
    """
    Algorithm for sorting an array
    Input: Unordered array
    Output: Ordered array
    Algorithm: choose a pivot (tipically random item in the array)
               create an array of items smaller than the pivot 
               create an array of items larger than the pivot 
               repeate 3 steps until sub-arrays have less than 2 items 
               add all arrays together
    """
    if len(array) < 2:
        return array      # Base case: arrays with 0 or 1 element are already “sorted.”
    else:  
        pivot = array[0]  # Recursive case
        less = [i for i in array[1:] if i <= pivot]     # Sub-array of all the elements less than the pivot
        greater = [i for i in array[1:] if i > pivot]   # Sub-array of all the elements greater than the pivot
    
        return quicksort(less) + [pivot] + quicksort(greater) 

print(quicksort([10, 5, 2, 3]))

