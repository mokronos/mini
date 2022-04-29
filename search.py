def linear(input, target):
    for idx, entry in enumerate(input):
        if entry == target:
            return idx
    return -1

def binary(input, target, idx = None):
    
    length = len(input)

    if length == 0:
        return -1

    middle = length//2

    if idx == None:
        idx = middle

    if input[middle]==target:
        return idx

    if input[middle]>target:
        return binary(input[:middle], target, idx-((middle//2)+1))
    else:
        return binary(input[middle+1:], target, idx+((middle//2)+1))

    




x = [3,1,4,5,9,6,2]
# x = ["apple","banana","pear","rock"]
y = 3
# y = "rock"

print(sorted(x))

# print(linear(x,y))

print(binary(sorted(x),y))

