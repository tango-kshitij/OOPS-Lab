l=[]
print("5 integers:")
for i in range(5):
    a=input()
    l.append(a)
res=sum(map(lambda x:int(x),l))
print(res)