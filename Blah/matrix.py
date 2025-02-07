count=0
matrix=[[0,1,1,0],
        [1,0,0,1],
        [1,1,1,1],
        [0,1,1,0]]

print(len(matrix))

rows=len(matrix)
cols=len(matrix)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
        if(j<len(matrix)-1):
            if ((matrix[i][j] == 1 and matrix[i][j + 1] == 1)):
                count += 1
        else:
            if(matrix[i][0]==1 and matrix[i][len(matrix)-1]==1):
                count+=1
    print()

print(count)

