# coading exercise page:59
# 4.1 write the code for the erlier sum function.
def summation(arr):
    total=0
    for item in arr:
        total+=item
    return total
# print(summation([1,2,3,4]))
# 4.2 Write a recursive function to count the number of items in a list ?
# thaught ,here list is an arr
def n_of_item(arr):
    if len(arr)<2:
        return 1
    return 1+n_of_item(arr[1:])
# print(n_of_item([1,2,3,7,8,9]))

#4.3 Find The Maximum Number In A List
def max_number(arr):
    max = arr[0]
    for item in arr:
        if item>max:
            max=item
    return max

# 4.4 Write Binary Search With Recursion
# def bin_rec(arr ,target):
#     mid = len(arr)//2
#     print("Mid",mid)
#     print("arr",arr)
#     if len(arr)<1:
#         return None
#     else:
#         if target==arr[mid]:
#             return mid
#         elif target < arr[mid]:
#             return bin_rec(arr[0:mid],target)
#         elif target>arr[mid]:
#             return bin_rec(arr[mid+1:],target)
            
def binarySearch(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = low + (high - low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, high, x)

    # Element is not present in the array
    else:
        return -1


# Driver Code
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10
    
    # Function call
    result = binarySearch(arr, 0, len(arr)-1, x)
    
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")



