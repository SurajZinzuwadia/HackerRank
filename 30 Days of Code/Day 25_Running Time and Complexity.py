n = int(input())
# for (i = 2; i*i <= n; i++){
#     //if divisible
#     if (n % i == 0)
#         NOT PRIME
# }
for _ in range(n):
    num = int(input())
    if(num == 1):
        print("Not prime")
    else:
        if(num % 2 == 0 and num > 2):
            print("Not prime")
        else:
            for i in range(3, int(num**(1/2))+1, 2):
                if num % i == 0:
                    print("Not prime")
                    break
            else:
                print("Prime")