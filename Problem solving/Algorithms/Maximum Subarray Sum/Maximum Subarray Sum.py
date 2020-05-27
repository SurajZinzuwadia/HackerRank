
import bisect

def maximumSum(a, m):
    mm,prefix=0,0
    temp=[]
    for i in a:
        prefix=(prefix+i)%m
        mm=max(mm,prefix)
        ind=bisect.bisect(temp,prefix)

        if(ind<len(temp)):
            mm=max(mm,prefix-temp[ind]+m)
        temp.insert(ind, prefix)
    print(mm)
if __name__ == '__main__':
    # fptr = open('Maximum_Subarray', 'w')

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)
    #
    #     fptr.write(str(result) + '\n')
    #
    # fptr.close()
