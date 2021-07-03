# class stackusingclass():
#     def__init__(self):
#         self.stack = []
#         return self.stack

#     def is_nil(seld, stack):
#         self.stack = stack
#         if(len(self.stack) == 0):
#             return True
#         return False
    
#     def push(self, stack, value)
#         self.stack = stack
#         self.value = Value
#         stack.append(value)

#     def pop(self, stack):
#         self.stack = stack
#         if is_nil(stack)
#             return "stack is nil"
#         return stack.pop()


class Stack():

    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def top(self):
        if len(self.item) >= 1:
            print self.item[len(self.item) -1]
        else :
            print "Empty list"

    def pop(self):
        if len(self.item) >= 1:
            self.item.pop()
        else:
            raise IndexError 

    def push(self,item):
        self.item.append(item)
        print self.item


new_stack = Stack()
new_stack.push(19)
new_stack.push(20)
new_stack.push(119)
new_stack.push(202)
new_stack.push(195)
new_stack.push(205)
new_stack.push(149)
new_stack.push(230)

print new_stack.size()
new_stack.top()
new_stack.pop()
new_stack.top()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.pop()
new_stack.top()