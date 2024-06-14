def swap(a,b,element):
    temp = element[a]
    element[a] = element[b]
    element[b] = temp

    return element



def lomuto_partition(element):
    pivot_index = len(element) - 1
    pivot = element[pivot_index]
    p_index = element[0]
    i = 0
 
    while pivot > element[i]:
        i += 1
    
    p_index = element[i]
    Counter = i

    while element[Counter] > pivot:
        Counter += 1

    swap(i,Counter,element)
    p_index = element[i]
    print(p_index)
    # return element

element = [11,9,29,7,2,15,28]
# print(lomuto_partition(element))
lomuto_partition(element)