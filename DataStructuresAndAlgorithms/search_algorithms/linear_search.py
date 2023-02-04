def linear_search(arr, x):
    for i, n in enumerate(arr):
        if n == x:
            return i
    return -1


index = linear_search([5, 2, 4, 1, 3], 4)
print(index)  # 2
