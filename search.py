# some search algorithms

def linear(input, target):
    for idx, entry in enumerate(input):
        if entry == target:
            return idx
    return -1

def binary(arr, target):

    low = 0
    high = len(arr)


    while low < high:
        middle = (low + high) // 2
        val = arr[middle]

        if val == target:
            return True
        elif val > target:
            high = middle
        else:
            low = middle + 1

    return False

def two_crystal():
    pass


x = [3,1,4,5,9,6,2]
x_sorted = [1,2,3,4,5,6,9]
# x = ["apple","banana","pear","rock"]

# y = "rock"

print(sorted(x))

# print(linear(x,y))

for y in x:
    print(binary(sorted(x),y))
