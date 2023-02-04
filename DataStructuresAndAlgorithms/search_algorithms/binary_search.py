def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


index = binary_search([1, 2, 3, 4, 5], 4)
print(index)  # 3
