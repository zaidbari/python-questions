x=int(input("Enter the number"))
y=str(x)
lst=list(y)
m=len(lst)
if(x<0):
    print("False")
elif(x==0):
    print("True")
else:
    flag=1
    for x in range((m+1)//2):
        if(lst[x]!=lst[m-1-x]):
            print("False")
            flag=0
    if(flag>0):
        print("True")
                
                
                
            
        