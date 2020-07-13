def powerSum(X,N,num):
    if(pow(num,N) < X):
        return powerSum(X,N,num+1) + powerSum(X-pow(num,N),N,num+1)
    elif(pow(num,N) == X):
        return 1
    else:
        return 0
X = int(input())
N = int(input())
print(powerSum(X,N,1))