def merge_sort(arr,key = 'time_hours',descending = True):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sort(left,right,arr,key,descending)

def merge_two_sort(a,b,arr,key,descending):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    if descending == False:
        while i < len_a and j < len_b:
        
            if a[i][key] < b[j][key]:
                arr[k] = a[i]
                i += 1
                k += 1
            else:
                arr[k] = b[j]
                j += 1
                k += 1
        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1
        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1

    else:
        while i < len_a and j < len_b:
            if a[i][key] > b[j][key]:
                arr[k] = a[i]
                i += 1
                k += 1
            else:
                arr[k] = b[j]
                j += 1
                k += 1

        while i < len_a:
            arr[k] = a[i]
            i += 1
            k += 1
        
        while j < len_b:
            arr[k] = b[j]
            j += 1
            k += 1
            
arr = [
    {'name':'vedanth','age':17,'time_hours':1},
    {'name':'rajab','age':12,'time_hours':3},
    {'name':'vignesh','age':21,'time_hours':2.5},
    {'name':'chinmay','age':24,'time_hours':1.5},
    {'name':'chinmay','age':24,'time_hours':1.45},
    {'name':'chinmay','age':24,'time_hours':0.5},
    {'name':'chinmay','age':24,'time_hours':4.5}

]
merge_sort(arr)
print(arr)