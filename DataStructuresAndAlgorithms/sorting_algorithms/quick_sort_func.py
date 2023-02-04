# To use this function: Call 'quick_sort' with the list you want to sort.

'''Example: 
            sorted_array = quick_sort([5, 2, 4, 1, 3])
            print(sorted_array)  # [1, 2, 3, 4, 5]
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
