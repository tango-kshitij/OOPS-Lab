n1=float(input("Enter 1st number: "))
n2=float(input("Enter 2nd number: "))
op=input("Enter the operator: ")
if op=='+':
    print(n1+n2)
elif op=='-':
    print(n1-n2)
elif op=='*':
    print(n1*n2)
elif op=='/':
    print(n1/n2)
elif op=='^':
    print(n1**n2)
else:
    print("Invalid operator used")