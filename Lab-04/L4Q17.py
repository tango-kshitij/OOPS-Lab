n=int(input("Enter the number of rows: "))
a=n
lim=1
for i in range(n):
    index=0
    k=i+1
    for j in range(a):
        print(" ",end=" ")
        index+=1
    for j in (lim):
        if index<n:
            print(k,end=" ")
            k+=1
            index+=1
        else:
            print(k,end=" ")
            k+=1
            index+=1
    a-=1
    lim+=2
    print("")