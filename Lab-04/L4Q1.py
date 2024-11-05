num=input("Enter the number: ")
sum=0
for i in range (len(num)):
    sum+=int(num[i])**(i+1)
if sum==int(num):
    print(f"{num} is a disarium number")
else:
    print(f"{num} is not a disarium number")