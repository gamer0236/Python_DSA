def linear_search(numberlist,indexofnum):
    for index,element in enumerate(numberlist):
        if element == indexofnum:
            return index
        
        
def binary_serach(numberlist,indexofnum):

    left_index = 0
    right_index = len(numberlist) - 1

    while left_index <= right_index:
        
        mid_index = (left_index + right_index) // 2
        mid_number = numberlist[mid_index]

        if  mid_number == indexofnum:
            return mid_index
    
        if mid_number < indexofnum:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1





numberlist = [1,2,3,4,5,6,7,8]
# print(linear_search(numberlist,8))
print(binary_serach(numberlist,5))