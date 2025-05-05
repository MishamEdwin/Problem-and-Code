A = "gksrek"
B = "geeksforgeeks"

new_b=""
ptr=0

print(A)
print(B)
for char in B:
    if ptr < len(A):
        if A[ptr]==char:
            new_b+=char
            ptr+=1


print(A)
print(new_b)

if A==new_b:
    print(1)
else:
    print(0)



