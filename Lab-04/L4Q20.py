n=int(input("Enter the number of rows: "))
k=1
for i in range(n):
    for j in range(i+1):
        print(j,end=" ")
        k+=1
    print("")

