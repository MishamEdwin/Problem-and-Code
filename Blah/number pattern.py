n=6
nums=list(range(6*6))
print(nums)

#1st 2 rows

top=int((n/2)-1)
print(top)

k=n
for i in range(1,top+1):
    if i==1 or i==2:
        print(" ",end="")

    val=i
    for j in range(n-i+1):
        print(" ",nums[val],end="")
        val+=1+k-i
        k-=1
    print()









"""

n=6
nums=list(range(6*6))
print(nums)
k=n

for i in range(1,n+1):
    if i==1 or i==2:
        print(" ",end="")

    val=i

    for j in range(n-i+1):
        print(nums[val],end=" ")
        val = nums[val]+k
        k-=1
    print("")











n = 6

# Outer loop for rows
for i in range(1, n + 1):
    # Add spaces for the first two rows
    if i == 1 or i == 2:
        print("   ", end="")  # Print 3 spaces for the first two rows

    num = i  # Start with the row number
    # Inner loop for columns in the current row
    for j in range(n - i + 1):  # The number of columns to print decreases with each row
        print(num, end=" ")  # Print the current number followed by a space
        num += n - j - 1  # Calculate the next number based on the column

    print()  # Move to the next line after printing all numbers in the row"""
