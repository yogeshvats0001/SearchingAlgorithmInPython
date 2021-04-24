#defining the function
def LinearSearch(myLst, key):
    for i in myLst:
        if i == key:
            return myLst.index(i)
    return -1

#defining the function for the st/nd/rd/th
def LocPos(loc):
    if loc == 1:
        return "st"
    elif loc == 2:
        return "nd"
    elif loc == 3:
        return "rd"
    else:
        return "th"

#empty list
myLst = []

#enter the number of elements for list
n = int(input("Enter the number of elements for list:"))

#values for elements
for i in range(n):
    myLst.append(int(input()))

#key
key = int(input("Enter the key which we have to search:"))

#calling the LinearSearch function
loc = LinearSearch(myLst, key)

#specify the position of element in  the list
if loc == -1:
    print(f"{key} is not found in the list")
else:
    loc += 1
    pos = LocPos(loc)
    print(f"{key} element is found at {loc} {pos} position in the list")