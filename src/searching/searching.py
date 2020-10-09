# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    while start <= end:
    
        # get middle
        midpoint = (start + end) // 2

       # searching left side 
        if target < arr[midpoint]: 
            
            return binary_search(arr, target, start, (midpoint-1))

        # searching right side
        elif target > arr[midpoint]: 
            
            return binary_search(arr, target, (midpoint+1), end)
        
        # if target is midpoint
        else: 
            return midpoint

     # if not in array
    return -1    


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass