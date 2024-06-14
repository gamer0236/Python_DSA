from collections import deque

stack = deque()
word = "we will conquere COVID-19"

for i in word:
    stack.append(i)

newlist = ''

while len(stack) != 0:
    newlist += stack.pop()


print(newlist)


