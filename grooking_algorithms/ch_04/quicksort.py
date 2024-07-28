# quicksort uses recursion
def qsort(arr):
    print("arr at first : ", arr)
    if len(arr)<2:
        return arr
    pivot = arr[0]
    print("Pivot",pivot)
    less = [i for i in arr[1:] if i <=pivot]
    print("less",less)
    greater = [i for i in arr[1:] if i > pivot]
    print("greater",greater)
    print("-------------------------------------------")
    return qsort(less)+[pivot]+qsort(greater)


print(qsort([8,5,7,3]))


# qucksort done bestly :)