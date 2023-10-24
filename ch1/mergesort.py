def merge(arr_a, arr_b):
    output = []
    length = len(arr_a) + len(arr_b)
    i = 0
    j = 0
    for k in range(length):
        if i >=len(arr_a):
            output.append(arr_b[j])
            j += 1
            continue
        elif j >= len(arr_b):
            output.append(arr_a[i])
            i += 1 
            continue
        if arr_a[i] < arr_b[j]:
            output.append(arr_a[i])
            i += 1
        else:
            output.append(arr_b[j])
            j += 1
    return output


def mergesort(Arr):
    if len(Arr) <= 1:
        return Arr
    midpoint = len(Arr) // 2
    front = Arr[:midpoint]
    back = Arr[midpoint:]
    sorted_front = mergesort(front)
    sorted_back = mergesort(back)
    Arr =  merge(sorted_front, sorted_back)
    return Arr


test_array = [5,4,1,8,7,2,6,3]
sorted_array = mergesort(test_array)
# print(mergesort(test_array))
# prints [1, 2, 3, 4, 5, 6, 7, 8]
print(test_array)
print(sorted_array)

#all one function, mutate the original array:

def mergesort_mutate(arr):
    length = len(arr)
    if length <= 1 :
        return arr
    midpoint = length // 2
    front = mergesort_mutate(arr[:midpoint])
    back = mergesort_mutate(arr[midpoint:])
    i = 0
    j = 0
    for k in range(length):
        if i >=len(front):
            arr[k] = back[j]
            j += 1
            continue
        elif j >= len(back):
            arr[k] = front[i]
            i += 1 
            continue
        if front[i] < back[j]:
            arr[k] = front[i]
            i += 1
        else:
            arr[k] = back[j]
            j += 1
    return arr

test_array2 = [5,4,1,8,7,2,6,3,100]
print(test_array2)
mergesort_mutate(test_array2)

print(test_array2)