n=int(input("Enter the number of rows: "))
k=1
lim=1
for i in range(n):
    for j in range(lim):
        if k%2==1:
            print("A",end=" ")
        else:
            print("B",end=" ")
    k+=1
    lim+=2
    print("")