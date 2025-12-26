# Given an array of integers nums, return the second-largest element in the array. If the second-largest element does not exist, return -1.


# Example 1

# Input: nums = [8, 8, 7, 6, 5]

# Output: 7

# Explanation:

# The largest value in nums is 8, the second largest is 7

x=int(input())
arr=list(map(int,input().split()))
lar = -9999
sec_lar = -9999

for i in range (x):
    if arr[i] > lar:
        sec_lar=lar
        lar=arr[i]

    elif (arr[i] < lar and arr[i] > sec_lar ) :
        sec_lar=arr[i]

if sec_lar == -9999:
    print("-1")

else:
    print(sec_lar)