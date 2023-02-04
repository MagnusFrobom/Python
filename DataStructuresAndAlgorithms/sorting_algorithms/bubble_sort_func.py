#  To use this function, Call 'bubble_sort()
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Example
sorted_array = bubble_sort([5, 2, 4, 1, 3])

print(sorted_array)  # [1, 2, 3, 4, 5]
