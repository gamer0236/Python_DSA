def bubble_sort(elements,key = 'name'):
    
    size = len(elements)

    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                swapped = True
        if not swapped:
            break
    for i in range(len(elements)):
        print(elements[i])
   



elements = [
    {'name': 'mona','transaction_amount':1000,'device':'iphone-10'},
    {'name':'dhaval','transaction_amount':400,'device':'google pixel'},
    {'name':'kathy','transaction_amount':200,'device':'vivo'},
    {'name':'aamir','transaction_amount':800,'device':'iphone-8'}
]

# bubble_sort(elemenets,key='transaction_amount')
bubble_sort(elements)