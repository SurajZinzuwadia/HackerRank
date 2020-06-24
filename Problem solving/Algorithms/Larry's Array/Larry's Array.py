
def rotate(arr):
    return arr[1:] + arr[:1]

def larrysArray(A):
    ct = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i]>A[j]:
                ct+=1
    if(ct%2):
        return "NO"
    else:
        return "YES"
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))
        result = larrysArray(A)