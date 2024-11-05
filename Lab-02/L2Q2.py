from statistics import *
num=[]
print("Enter 25 numbers: ")
for i in range(25):
    n=float(input())
    num.append(n)
mean_val=mean(num)
median_val=median(num)
try:
    mode_val=mode(num)
except:
    mode_val="No unique value"
print(mean_val)
print(median_val)
print(mode_val)