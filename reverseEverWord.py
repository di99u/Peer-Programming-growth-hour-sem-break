# Reverse Every Word in A String



# 0

# Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). A word is defined as a sequence of non-space characters. The words in s are separated by at least one space.

# Return a string with the words in reverse order, concatenated by a single space.

s=input()
n=len(s)
arr=[]
res=''
row=''

for i in range(n):
    
    if s[i]==" ":

        if row!='' :
            arr.append(row)
            row=''

    else:
        row+=s[i]

    # while s[i]!=" " and i<n:
    #     row += s[i]
    #     i+=1
if row!='':
    arr.append(row)

res=arr[::-1]
print(' '.join(res))