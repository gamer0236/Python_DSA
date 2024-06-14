number = int(input("enter number:- "))
oddlist = []

for num in range(number):
    if num % 2 != 0:
        oddlist.append(num)
    else:
        pass

print(oddlist)


