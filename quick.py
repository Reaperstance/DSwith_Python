def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    p = arr[len(arr) // 2]  
    left = []  
    mid = []  
    right = []  
    
    for x in arr:
        if x < p:
            left.append(x)
        elif x == p:
            mid.append(x)
        else:
            right.append(x)
    
    return quicksort(left) + mid + quicksort(right)

arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sorted array:", quicksort(arr))
