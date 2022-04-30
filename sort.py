# some sorting algorithms

def selection(input):

    for i in range(len(input)):

        min_idx = i
        for j in range(i,len(input)):
            if input[j] < input[min_idx]:
                min_idx = j
        
        input[i], input[min_idx] = input[min_idx], input[i]

    return input

def bubble(input):

    for i in range(len(input)):
        for j in range(len(input)-i-1):
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]


    return input

def merge(input):

    if len(input)==1:
        return input

    middle = len(input)//2

    left, right = input[:middle], input[middle:]

    left = merge(left)
    right = merge(right)

    result=[]

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    if i < len(left):
        result += left[i:]

    if j < len(right):
        result += right[j:]

    return result

x = [3,1,4,5,9,6,2]
# print(selection(x))
print(merge(x))
