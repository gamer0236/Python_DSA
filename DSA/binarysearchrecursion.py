def binary_recursion(numberlist,indexofnum,left_index,right_index):

    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2

    if mid_index >= len(numberlist) or mid_index < 0:
        return -1
    
    mid_number = numberlist[mid_index]

    if mid_number == indexofnum:
        return mid_index
    if mid_number < indexofnum:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_recursion(numberlist,indexofnum,left_index,right_index)

numberlist = [1,2,3,4,5,6,7,8]
print(binary_recursion(numberlist,1,0,len(numberlist) - 1))
































# class Binaryserach:
#     def __init__(self,numberlist):
#         self.numberlist = numberlist
        
#     def binary_search(self,indexofnum):
#         left_index = 0
#         right_index = len(self.numberlist) - 1
#         mid_index = (left_index + right_index) // 2
#         mid_number = self.numberlist[mid_index]

#         if mid_number == indexofnum:
#             return mid_index
        
#         if mid_number < indexofnum:
#             # left_index = left_index + 1
#             newlist = self.numberlist[mid_index:right_index]
#             self.numberlist = newlist
#             return self.binary_search(indexofnum)

#         else:
#             # right_index = right_index - 1
#             newlist = self.numberlist[mid_index:right_index]
#             self.numberlist = newlist
#             return self.binary_search(indexofnum)


        
# numberlist = [1,2,3,4,5,6,7,8,9]
# node = Binaryserach(numberlist)
# print(node.binary_search(8))

