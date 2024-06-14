def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    rigth  = arr[mid:]

    left = merge_sort(left)
    rigth = merge_sort(rigth)

    return merge_two_sort(left,rigth)

def merge_two_sort(a,b):
    sorted_list = []

    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1

    return sorted_list


a = [5,6,7,8,9]
b = [1,2,3,4]
arr = [10,3,15,7,8,23,98,29]
print(merge_two_sort(a,b))
print(merge_sort(arr))