
def binary_search(list_1, target_value):

    low = 0
    high = len(list_1)-1

    while low <= high:
        mid = (low + high) // 2

        if list_1[mid] == target_value:
            print("value found at index",mid)
            return
        if list_1[mid] < target_value:
            low = mid + 1
            
        if list_1[mid] >target_value:
            high = mid - 1

    print("Value is not found")

list_1 = [3, 4, 5, 6, 7, 8, 9, 10]
binary_search(list_1, target_value = 10)
