l1=[1,3,5,7]
l2=[2,8,16,91]

def add(a,b):
    return a+b

def subt(a,b):
    return b-a
ares=list(map(add,l1,l2))
sres=list(map(subt,l1,l2))
print("Add: ",ares,"\nSubtract: ",sres)
