n=int(input("Enter the number of rows: "))
a=n
lim=1
for i in range(n):
    index=0
    if i>0:
        lim+=2
    for j in range(a):
        print(" ",end=" ")
        index+=1
    for j in (lim):
        print("*",end="")
    a-=1
    print("")