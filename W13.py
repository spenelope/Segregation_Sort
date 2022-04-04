def sort_recursive(array, start, end):

    pivot = array[end]
    i = start - 1

    for j in range(start, end):
        if array[j] <= pivot: # swap the value if element smaller than pivot 
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[end]) = (array[end], array[i + 1])
    return i + 1

def sort(array, start, end):
    if start < end:         
        # left - value < pivot 
        # rigth - value > pivot
        check = sort_recursive(array, start, end)
        sort(array, start, check - 1)
        sort(array, check + 1, end)

#Test
values = [31, 72, 10, 32, 18, 95, 25, 50]
empty = []
singular = [12]
swapping = [99, 40, 15] 
duplicates = [4, 4, 80, 77, 60]
large = [4, 15, 82, 96, 33, 44, 44, 2, 1, 45,79, 33, 33, 33, 22, 15]

print("Before sorting the Array:")
print(values)
print(empty)
print(singular)
print(swapping)
print(duplicates)
print(large)

size = len(values)
sort(values, 0, size - 1)

size = len(empty)
sort(empty, 0, size - 1)

size = len(singular)
sort(singular, 0, size - 1)

size = len(swapping)
sort(swapping, 0, size - 1)

size = len(duplicates)
sort(duplicates, 0, size - 1)

size = len(large)
sort(large, 0, size - 1)


print("After sorting the Array:")
print(values)
print(empty)
print(singular)
print(swapping)
print(duplicates)
print(large)