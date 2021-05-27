# define a function named as binary_Search which accepts two parameters
def binary_Search(lst, key):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] > key:
            high = mid -1
    
        elif lst[mid] < key:
            low = mid + 1
    
        else:
            return mid
    return -1


# input from user for number of elements
n = int(input("Enter the number of elements: \n"))

# create an empty list
lst = []

# save the values into lst from user (Must be in sorted order)
for i in range(n):
    lst.append(int(input(f"Enter the values at {i} place: \n")))

# enter the key value from the user
key = int(input("Enter the key value: \n"))

# calling the defined function
pos = binary_Search(lst, key)

if pos != -1:
    print(f"Position of key element in the list(starting from 0th index): {pos}")
else:
    print("Please check the entered key")