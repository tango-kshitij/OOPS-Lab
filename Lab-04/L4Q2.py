num=input("Enter the number: ")
sum=0
for i in range (len(num)):
    sum+=int(num[i])
if int(num)%sum==0:
    print(f"{num} is a Harshad number")
else:
    print(f"{num} is not a Harshad number")