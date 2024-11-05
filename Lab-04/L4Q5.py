def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter value of 'n': "))
r=int(input("Enter value of 'r': "))
ans=fact(n)//(fact(n-r)*fact(n))
print(f"nCr of given values is {ans}")