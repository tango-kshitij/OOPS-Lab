n=int(input("Enter the number of rows: "))
k=1
lim=1
for i in range(n):
    for j in range(lim):
        if k%2==1:
            print("1",end=" ")
        else:
            print("0",end=" ")
    k+=1
    lim+=2
    print("")