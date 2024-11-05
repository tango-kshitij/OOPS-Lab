def fun(a):
    try:
        return int(a)
    except:
        return a

tup=('a','9','hi','27')
res=list(map(fun,tup))
print(res)