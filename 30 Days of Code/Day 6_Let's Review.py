# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(0,n):
    name = input().strip()
    print(name[::2],name[1::2])