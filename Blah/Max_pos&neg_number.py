"""This program checks that which max positive integer in an array has its own negative integer """
from sympy import true, false

n=int(input("Enter the size:"))
numb_arr=[]

for i in range(0,n):
    elem=int(input("Enter the element:"))
    numb_arr.append(elem)

numb_arr.sort()
print(numb_arr)

max_positive_num=numb_arr[-1]

print(max_positive_num)

found = false
for i in range(0,n):
    if numb_arr[i]== -max_positive_num:
        print("True")
        found = true

if not found:
    print("False")










