

def search(list, n):
    i = 0

    while i< len(list):
        if list [i] == n:
            return True
        i = i + 1

    return False


list = [3, 4, 6, 1 ,3 ,8, 9]
n = 8

if search(list, n):
    print("Found")
else:
    print("Not Found")





list = [4, 5, 8, 9, 0, 2, 7]
n = 2
t = 0
for i in list:
    if i == n:
        t = 1
        

if t == 1:
    print ("Found at index number", list.index(i))
else:
    print ("Not Found")
    


