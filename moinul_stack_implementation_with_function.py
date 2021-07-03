def create_stack():
    stack = []
    return stack

def is_empty(stack):
    if len(stack) == 0:
        return True
    return False

def insert(stack, insert_value):
    stack.append(insert_value)

def delete(stack):
    if is_empty(stack):
        return 'stack is empty'

    return stack.pop()


stack = create_stack()
insert(stack, 78)
insert(stack, 90)
insert(stack, 56)
insert(stack, 23)
print('After insert', stack)
delete(stack)
print('After delete', stack)
print('After delete', stack)