def prime(n):
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
    if flag:
        return True
    else:
        return False
def smith(num):
    temp=num
    l=[]
    for i in range(2,temp):
        if prime(i):
            if num%i==0:
                l.append(i)
                num=num//i
    p=0
    for i in l:
        if i<9:
            p+=i
        else:
            i=str(i)
            for j in i:
                p+=int(j)      
    s=0
    temp=str(temp)
    for i in temp:
        s+=int(i)
    if s==p:
        print("number is smith number")
    else:
        print("number is not smith number")
n=int(input("enter number"))
smith(n)
