n=int(input("Enter the number of rows: "))
b=n
space=0
for i in range(n):
    for j in range(space):
        print(" ",end=" ")
    for j in (1+(b-1)*2):
        print("*",end=" ")
    b-=1
    space+=1
    print("")