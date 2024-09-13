
# Binary Search following an Iterative Method:
def binarySearch(arr, k, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Grokking's Binary Search Algorithm
def grokkings_binary_search(list, item): 
    low = 0
    high = len(list) - 1
    while low <= high: 
        mid = (low + high) 
        guess = list[mid] 
        if guess == item:
            return mid
        if guess > item: 
            high = mid - 1
        else:
            low = mid + 1
    return None

# Binary search using Recursion:
def RbinarySearch(arr, k, low, high):
    if high >= low:
        mid = low + (high - low)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            return RbinarySearch(arr, k, low, mid-1)
        else:
            return RbinarySearch(arr, k, mid + 1, high)
    else:
        return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    k = 7  # Value to be searched

    # Applying Iterative Binary Search  
    result = binarySearch(arr, k, 0, len(arr)-1)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")

    #  Applying Recursive Binary Search
    result = RbinarySearch(arr, k, 0, len(arr)-1)
    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("Not found")
 

