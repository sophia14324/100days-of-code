def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    partition = arr[0]  
    less = []  
    greater = []  

    # Partition the array into two subarrays: elements less than or equal to partition, and elements greater than partition
    for i in range(1, len(arr)):
        if arr[i] <= partition:
            less.append(arr[i])
        else:
            greater.append(arr[i])

    return quick_sort(less) + [partition] + quick_sort(greater)

my_list = [8, 3, 1, 5, 2, 7, 9, 4]
sorted_list = quick_sort(my_list)
print(sorted_list)  