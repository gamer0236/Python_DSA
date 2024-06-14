def bubble_sort(numberlist):

    size = len(numberlist)
    for i in range(size-1):
        swapped = False
        for j in range(size - 1-i):
            if numberlist[j] > numberlist[j + 1]:
                temp = numberlist[j]
                numberlist[j] = numberlist[j + 1]
                numberlist[j + 1] = temp
                swapped = True
        if not swapped:
                break
    return numberlist

numberlist = [4,6,2,8,4,9,7,3]
print(bubble_sort(numberlist))