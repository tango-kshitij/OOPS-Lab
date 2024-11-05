num=int(input("Enter the number"))
for i in range (1,num/2):
    if num%i==0:
        sum+=i
if sum==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")