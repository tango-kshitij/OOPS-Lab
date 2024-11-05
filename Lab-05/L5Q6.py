seq=input("Sequence: ")
ures=list(map(lambda a:a.upper(),set(seq)))
lres=list(map(lambda a:a.lower(),set(seq)))
print("Uppercase: ",ures,"\nLowercase: ",lres)