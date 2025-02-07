"""This program gets an input value as n and should contain n elements whose addition value equals zero"""

n=int(input("Input = "))
numb_arr=[]

total=0
new_total=0

for i in range(0,n-1):
    numb_arr.append(i)

#print(numb_arr)

for elem in numb_arr:
    total = total + elem
#print(total)

numb_arr.append(-total)

print(numb_arr)

for new_elem in numb_arr:
    new_total = new_total + new_elem

print(new_total)