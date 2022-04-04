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
print("Before sorting the Array:")
print(values)

size = len(values)
sort(values, 0, size - 1)

print("After sorting the Array:")
print(values)