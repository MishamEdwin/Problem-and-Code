n=20
first=0
second=1


print(first,second,end=" ")
for i in range(1,n-1):
    temp=first+second
    print(temp,end=" ")
    first=second
    second=temp

"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144"""