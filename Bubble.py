# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

def bubble_sort(n,arr):
    
    for i in range(n):

        for j in range(n-i-1):

            if(arr[j] > arr[j+1]):

                arr[j],arr[j+1]=arr[j+1],arr[j]



n=int(input())
arr=list(map(int,input().split()))
bubble_sort(n,arr)

print(arr)