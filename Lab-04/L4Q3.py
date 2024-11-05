for i in range (100):
    a=str(i)
    sum=0
    for j in range (len(a)):
        sum+=int(a[j])**3
    if i==sum:
        print(i)