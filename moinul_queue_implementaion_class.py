class Queue():
#Implementation Queue with Class#
    def __init__(self):
        self.queue = []
        self.max_length = 10

    def display(self):
        print("Queue = ", self.queue)

    def peek(self):
        print(self.queue[0])

    def is_empty(self):
        if len(self.queue) == 0:
            print("Oops!Your Que is Empty")
        else:
            print("Queue is not Empty")

    def is_full(self):
        if len(self.queue) == self.max_length:
            print("Oops!Queue is Full")
        else:
            print("Queue is not full")

    
    def enqueue(self, value):
        if (len(self.queue) == self.max_length):
            print("Oops!Queue is Full")
        else:
            self.queue.insert(0, value)
    
    def dequeue(self):
        if (len(self.queue) == 0):
            print("Oops!Queue is Empty")
        
        else:
            self.queue.pop(0)

       
obj = Queue()
obj.enqueue(34)
obj.enqueue(56)
obj.enqueue(78)
obj.enqueue(89)
obj.enqueue(23)
obj.enqueue(71)
obj.enqueue(92)
obj.enqueue(80)
obj.enqueue(83)
obj.enqueue(20)
obj.display()
obj.peek()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.dequeue()
obj.display()
obj.is_empty()
obj.is_full()

