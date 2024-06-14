# deque is the recommended way to implement a stack in python

from collections import deque

stack = deque()
stack.append(34)
stack.append(345)
stack.append(65434)

print(stack.pop())
print(stack.pop())
print(stack[-1])

