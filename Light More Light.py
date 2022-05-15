no_of_light=int(input("enter no of light"))
status=int(input("enter which light statusyou want"))
flag=False
for i in range(1,status+1):
    if status%i==0 and flag==False:
        flag=True
    elif status%i==0 and flag==True:
        flag=False
if flag==False:
    print("light is off")
else:
    print("light is on")

