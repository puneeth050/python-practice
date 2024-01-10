def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    print(low, high)
    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid 
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_arr = [1,2,3,4,5,6,7,8,9,10]
target_value = 6
result = binary_search(sorted_arr, target_value)

if result != -1:
    print(result)
else:
    print('Not found')