# Problem Statement: Given an array of integers arr[] and an integer target.

# 1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.


x = int(input())

arr = list(map(int, input().split()))

target = int(input())

sum_present = False

for i in range(x-1):
    for j in range(i+1, x):
        sum = arr[i] + arr[j]
        if sum == target:
            sum_present = True

if sum_present:
    print("Yes")
else:
    print("No")
