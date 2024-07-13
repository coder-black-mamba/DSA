# self implementation without anything before
# check if current is bigger then element

# def binary_search(arr,element):
#     length = len(arr)
#     initial_index=int(length/2)
#     step=1
#     # cause at the end of the day it has to be one
#     print("Length = ",length,"Initial Index ",int(initial_index))
#     while not (initial_index <=1):
#         print("Step = ",step)
#         print("Intitial Index Inside ", initial_index)
#         print("Intitial arr ", arr)
#         print("Intitial arr(initial_index) ", arr[initial_index])
#         if arr[initial_index] == element:
#             return initial_index
#         elif arr[initial_index] < element:
#             print(arr)
#             arr=arr[initial_index:]
#             print(arr)

#         elif arr[initial_index] > element:
#             arr = arr[0:initial_index]
#         print(initial_index)
#         initial_index=int(initial_index/2)
#         print(initial_index)
#         step+=1
#     return None
        

# arr = [1,2,3,4,5]
# # Good But Does Not Work With Odd Length (Have To Have Fix IT later)
# print("Retunrn Value Of Bin Search : ",binary_search(arr,3))

# Book Implementation
# def binary_search(arr,element):
#     low = 0
#     high = len(arr)-1
#     while low <= high:
#         print("Low",low)
#         print("high",high)
#         mid = int((low+high)/2)
#         print("mid",mid)
#         guess = arr[mid]
#         if guess == element:
#             return mid
#         if guess>element:
#             high = mid-1
#         else:
#             low=mid+1
#         return None

def search_iterative( list, item):
    # low and high keep track of which part of the list you'll search in.
    low = 0
    high = len(list) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
      # ... check the middle element
      mid = (low + high) // 2
      print("mid",mid)
      guess = list[mid]
      # Found the item.
      if guess == item:
        return mid
      # The guess was too high.
      if guess > item:
        high = mid - 1
      # The guess was too low.
      else:
        low = mid + 1

    # Item doesn't exist
    return None

arr = [5,6,87,56,45]
# Again Good But Does Not Work With Odd Length (Have To Have Fix IT later)
print("Retunrn Value Of Bin Search : ",search_iterative(arr,5))



