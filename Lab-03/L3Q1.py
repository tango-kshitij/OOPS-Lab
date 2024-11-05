n=int(input("Enter a number: "))
flag=1
if n>1:
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            flag=0
            break
elif n==1:
    flag=0

if flag==1:
    print("Prime")
else:
    print("Not prime")