import time
import threading
from collections import deque

queue = deque()

def place_order(orders):
    for item in orders:
        print("placing order for:- ",item)
        queue.appendleft(item)
        time.sleep(0.5)
        

def serve_order():
    time.sleep(1)
    while len(queue) != 0:
        print(f"now serving:- {queue.pop()}")
        time.sleep(2)

orders = ["pizza","samosa","pasta","biriyani","burger"]

# place_order(orders)
# serve_order()
t = time.time()

t1 = threading.Thread(target= place_order,args= (orders,))
t2 = threading.Thread(target= serve_order,)

t1.start()
t2.start()

t1.join()
t2.join()

print("done in: ",time.time()-t)
print("done")
