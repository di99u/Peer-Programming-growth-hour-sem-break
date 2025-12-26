# # Given an array of integers nums, sort the array in non-decreasing order using the selection sort algorithm and return the sorted array.



# A sorted array in non-decreasing order is an array where each element is greater than or equal to all previous elements in the array.


# Example 1

# Input: nums = [7, 4, 1, 5, 3]

# Output: [1, 3, 4, 5, 7]

# Explanation: 1 <= 3 <= 4 <= 5 <= 7.

# Thus the array is sorted in non-decreasing order.

def selection_sort(x,arr):

    for i in range(x):
        min_index=i
        for j in range(i+1,x):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index] , arr[i]
    return



x = int(input())
arr=list(map(int,input().split()))
selection_sort(x,arr)
print(arr)