n = [12, 8, 1, 6, 2]
arrange = []
studs = n[0]

# Calculate the number of rows as half the number of students
rows = int(studs /2)
print(rows)

cols = 2
value = 1

# Loop to create 6 pairs
for i in range(rows):
    desk = [value, value + 1]
    arrange.append(desk)
    value += 2

for i in arrange:
    print(i)

occupied=n[1:]
print(occupied)

print(arrange)
print(len(arrange))
for i in range(len(arrange)):
    for j in range(cols):
        if(arrange[i][j] in occupied):
            arrange[i][j]=0

for i in arrange:
    print(i)

horizontalcount=0
for rows in arrange:
    if(rows[0]!=0 and rows[1]!=0):
        horizontalcount+=1
print("Horizontal Count = ",horizontalcount)

verticalcount=0
for col in range(2):
    for row in range(len(arrange)-1):
        if(arrange[row][col]!=0 and arrange[row+1][col]!=0):
            verticalcount+=1
print("Vertical Count = ",verticalcount)