n=int(input("enter size"))
arr= list(map(int,input("enter array elements").split()))
is_sorted= True

for i in range(n-1):
    if(arr[i]>arr[i+1]):
        is_sorted= False
        break

print(is_sorted)