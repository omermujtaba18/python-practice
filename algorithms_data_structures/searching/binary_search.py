"""Binary Search
if not found return -1 , 
else return index of found element"""


def binary_search(input_array, value):

    low = 0
    high = len(input_array) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if (input_array[mid] == value):
            return mid
        elif(input_array[mid] > value):
            high = mid-1
        else:
            low = mid+1

    return -1


def binary_search_recursive(input_array, value):
    mid = len(input_array)-1

    if(mid < 0):
        return -1
    elif(input_array[mid] == value):
        return mid
    elif(input_array[mid] > value):
        return binary_search_recursive(input_array[:mid-1], value)
    else:
        return binary_search_recursive(input_array[mid+1:], value)


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))

print(binary_search_recursive(test_list, test_val1))
print(binary_search_recursive(test_list, test_val2))
