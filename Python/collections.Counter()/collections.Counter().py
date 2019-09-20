from collections import Counter 
X = input() # number of shoes
shoesList = Counter(map(int,input().split())) # all shoes size
Customer = int(input())
result = 0
for i in range(Customer):
    (size,price) = map(int,input().split())
    if shoesList[size] > 0:
        shoesList[size]-=1
        result+=price
print(result)
