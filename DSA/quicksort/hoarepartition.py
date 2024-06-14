def swap(a,b,arr):
    if a!= b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp



def partition(element,start,end):
    pivot_index = start
    pivot = element[pivot_index]

    
    while start < end:
        while start < len(element) and element[start] <= pivot:
            start += 1

        while element[end] > pivot:
            end -= 1

        if start < end:
            swap(start,end,element)

    swap(pivot_index,end,element)

    return end

def quick_sort(element,start,end):
    
    if start < end:
        pi = partition(element,start,end)
        quick_sort(element,start,pi - 1) # left partition
        quick_sort(element,pi + 1,end) # right partition

element = [11,9,29,7,2,15,28]
quick_sort(element,0,len(element) -1)
print(element)