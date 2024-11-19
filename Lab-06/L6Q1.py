num=list(map(int(input("Enter numbers seperated by space: ").split())))
to_ap=int(input("Enter a number to append: "))
num.append(to_ap)
print("Num: ")

to_ins=int(input("Enter a number to insert: "))
pos=int(input("Enter a position to insert at: "))
num.insert(pos,to_ins)
print("After insert: ",num)

num.pop()
print("After pop: ",num)
num.sort()
print("After sort: ",num)
num.reverse()
print("After reverse: ",num)
print("Length of Num: ",len(num))

