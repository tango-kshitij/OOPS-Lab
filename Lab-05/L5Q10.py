n=int(input("N: "))
count=0
a=0
b=1
fib=[]

while (count<n):
    fib.append(b)
    a,b=b,a+b
    count+=1
res = list(map(lambda x:x**2,fib))
print(res)