# Q1. Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Test the function
input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)
