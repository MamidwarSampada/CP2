def prime(n):
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
    if flag:
        return True
    return False
def sum_prime(n):
    l=[]
    for i in range(2,n):
        if prime(i):
            l.append(i)
    l.reverse()
    k=[]
    for i in l:
        for j in l:
            for m in l:
                for d in l:
                    if (i+j+m+d)==n:
                        k=[i,j,m,d]
                        print(k)
                        break
                    
    return k
n=int(input("enter number"))
print(sum_prime(n))

