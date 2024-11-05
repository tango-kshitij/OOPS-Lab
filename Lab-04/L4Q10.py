num=input("Enter the number")
l=str()
for i in range(len(num)):
    l+num[-i-1]
if l==num:
    print(f"{l} is palindrome")

