def insirtion_sort(numlist):
    for i in range(1,len(numlist)):
        anchor = numlist[i]
        j = i - 1
        while j >= 0 and anchor < numlist[j]:
            numlist[j + 1] = numlist[j]
            j = j - 1
        numlist[j + 1] = anchor
    return numlist

numlist = [1,2,55,34,7,6,9,20]
print(insirtion_sort(numlist))