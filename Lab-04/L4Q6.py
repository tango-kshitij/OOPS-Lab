a=0
b=1
n=int(input("Enter the number of iterations: "))
for i in range(n):
    print(f"{b}",end=" ")
    sum=a+b
    a=b
    b=sum