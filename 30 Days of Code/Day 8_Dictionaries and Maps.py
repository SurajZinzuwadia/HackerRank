# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
d = dict(input().strip().split() for _ in range(n))
query = []
while True:
    try:
        name = input().strip()
        if name in d:
            print(name,"=",d[name],sep="")
        else:
            print("Not found")
    except EOFError as error:
        break