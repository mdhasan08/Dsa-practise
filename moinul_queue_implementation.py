queue = []
max_len = 10
min_len = 0

def display():
    print("Queue = ", queue)

def peek():
    print(queue[0])
    print("Oops!Queue is Empty")


# Queue is Empty
def is_empty():
    if len(queue) == 0:
        print("Your Queue is Empty")

# is_empty()



def is_full():
    if len(queue) == max_len:
        print("Queue is Full")


def enque(value):
    if len(queue) == max_len:
        return("Oops!Queue is full")
    else:
            queue.insert(0, value)


# for deleting data form queue
def deque():
    if len(queue) == 0:
        return("Oops!Queue is Empty")

    else:
        queue.pop(0)


enque(56)
enque(78)
enque(13)
enque(24)
enque("r")
enque("u")
enque(12)
enque(67)
enque("o")
enque(87)
display()
is_empty()
is_full()
peek()
deque()
deque()
deque()
deque()
deque()
deque()
deque()
deque()
deque()
deque()
display()