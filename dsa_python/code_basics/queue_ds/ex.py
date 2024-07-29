from collections import deque
import time
import threading

class Queue:
    def __init__(self) -> None:
        self.buffer=deque()

    def enqueue(self,item):
        self.buffer.append(item)

    def dequeue(self):
        return self.buffer.popleft()

    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer)==0



# 1.question _01

queue=Queue()

def place_order(orders):
    for item in orders:
        queue.enqueue(item)
        time.sleep(0.5)
        print("Placing Order Form",item)

def serve_order():
    time.sleep(1)
    while True:
        if queue.size():
            to_be_served=queue.dequeue()
            print("Now Serving ",to_be_served)
            time.sleep(2)
        else:
            break

# orders = ['pizza','samosa','pasta','biryani','burger']

# order_thread=threading.Thread(target=place_order,args=[orders])
# service_thread=threading.Thread(target=serve_order)


orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)
# uncomment for start
# t1.start()
# t2.start()

# Godder ;)

# 2. Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in main tutorial. Binary sequence should look like,
def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()

produce_binary_numbers(10)

# Wrong Fix it later