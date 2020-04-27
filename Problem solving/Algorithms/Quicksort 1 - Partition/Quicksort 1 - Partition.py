def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = [p]
    result = []
    for i in range(1,n):
        p = arr[0]
        left = []
        right = []
        equal = [p]
        for i in range(1, len(arr)):
            if (p < arr[i]):
                right.append(arr[i])
            elif (p > arr[i]):
                left.append(arr[i])
            else:
                equal.append(arr[i])
        # if(len(left) > 1):
        #     left = quickSort(left)
        # if(len(right) > 1):
        #     right = quickSort(right)
        return (left + equal + right)
if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)
    print(' '.join(map(str, result)))
