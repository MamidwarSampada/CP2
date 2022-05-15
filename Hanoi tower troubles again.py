def square(n):
    l=[]
    for i in range(1,n+1):
        l.append(i*i)
    return l
import math
n=int(input("no of peg"))
b=int(input("no of balls"))
l=[]
for i in range(n):
    l.append([])
for i in range(1,b+1):  
    s=square(b*b) 
    for j in l:  
        if len(j)==0:
            j.append(i)
            break 
        elif j[-1]+i in s :
            j.append(i)
            break
print(l)

