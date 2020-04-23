def bonAppetit(bill, k, b):
    temp = bill[k]
    bill.remove(temp)
    print(bill)
    AnnaTotal = sum(bill)/2
    print(AnnaTotal)
    if(AnnaTotal == b):
        print("Bon Appetit")
    else:
        print(b - AnnaTotal)



if __name__ == '__main__':
    nk = input().strip().split()
    n = int(nk[0])
    k = int(nk[1])
    bill = list(map(int,input().strip().split()))
    b = int(input().strip())
    bonAppetit(bill, k, b)