def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap,size):
            anchor= arr[i]
            j = i
            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2


arr = [28,221,34,11,3,6]
shell_sort(arr)
print(arr)