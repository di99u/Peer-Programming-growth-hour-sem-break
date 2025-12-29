# Rotate Image by 90 degree



# 5

# Problem Statement: Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly..

x=int(input())

arr=[]

for i in range(x):
    row=list(map(int,input().split()))
    arr.append(row)

for i in range(x):
    for j in range(i+1,x):
        arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

for i in range(x):
    arr[i].reverse()

for row in arr:
    print(*row)