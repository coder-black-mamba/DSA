# O(n^2)
def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for index,item in enumerate(arr):
        if item<smallest:
            smallest = item
            smallest_index=index
    return smallest_index
            

# print(find_smallest([3,6,3453,25,25,9,1]))
def selection_sort(arr):
    new_arr=[]
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr



# print(selection_sort([3,2,6,7,5,37,36,1]))


def selection_sort_me(arr):
    new_arr=[]
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        # here i = 0 (it will run through all of tje arr element whatever the length is)
        # smallest = 3
        for item , index in enumerate(arr):
            if item < smallest:
                smallest = item
                smallest_index=index
        new_arr.append(arr.pop(smallest_index))      
    return new_arr    
print(selection_sort_me([3,2,6,7,5,37,36,1]))
