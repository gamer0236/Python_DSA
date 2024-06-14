
mydict = {}

file = open('poem.txt','r')
poem = file.read().split(' ')

for word in poem:
    occurence = poem.count(word)
    mydict.update({word:occurence})

print(mydict['I'])