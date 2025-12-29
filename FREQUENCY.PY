s=input()
counts={}

for char in s:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

Mx = max(counts.values())
Mn = min(counts.values())

Ma=[]
Mi=[]


for char in counts:
    if(counts[char]==Mx):
        Ma.append(char)
    if(counts[char]==Mn):
        Mi.append(char)

print("frq:",*Ma,Mx)
print(Mi)