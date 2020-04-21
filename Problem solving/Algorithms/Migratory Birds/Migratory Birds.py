def migratoryBirds(arr):
    count = [0] * len(arr)
    result = 0
    for i in arr:
        count[i] += 1
    result = count.index(max(count))
    return result
if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int,input().strip().split()))
    result = migratoryBirds(arr)
    # print(result)