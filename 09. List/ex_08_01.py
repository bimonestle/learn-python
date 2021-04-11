nums = [1,2,3,4,5]

def chop(arr):
    arr.pop(0)
    arr.pop()
    print("chop:",arr)
    return None

print(nums)
def middle(arr):
    lastInd = len(arr) - 1
    newList = arr[1:lastInd]
    print("middle:", newList)
    return newList

chop(nums)

nums = [1,2,3,4,5]
middle(nums)