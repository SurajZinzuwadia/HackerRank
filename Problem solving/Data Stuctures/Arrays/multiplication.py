N = list((input().split()))
print(N)
n = N[0]
print(n)
# N = int(input("Enter row number:")) # row
# M = int(input("Enter col number:")) # col
# # matrix variable for storing array
# matrix = []
# # For user input
# for i in range(N):          # A for loop for row entries
#     a =[]
#     for j in range(M):      # A for loop for column entries
#          a.append(int(input()))
#     matrix.append(a)
# print(matrix)
# k=0
# j=0
# temp = []
# #for upper half
# for i in range(N):
#     k=i
#     j=0
#     while(k>=0 and (j<=i and j<M)):
#         temp.append(matrix[k][j])
#         k-=1
#         j+=1
# #for lowwer half
# for i in range(0,N):
#     k = N-1
#     j = 1+i
#     while(k>=i and j<=M-1):
#         temp.append(matrix[k][j])
#         k-=1
#         j+=1
# print(temp)
# k=0
# #upper print logic
# for i in range(0,N-1):
#     for j in range(0,i+1):
#         print(temp[k],end=" ")
#         k+=1
#     print("\r")
# #lower print logic
# for i in range(0,N):
#     for j in range(0,M-i):
#         print(temp[k],end=" ")
#         k+=1
#     print("\r")