matrix=[[1, 2, 3,  4],
        [12,13,14, 5],
        [11,16,15, 6],
        [10, 9, 8, 7]]

result=[]

rowStart=0
colStart=0

rowEnd=len(matrix)
colEnd=len(matrix[0])

print(rowEnd,colEnd)

while rowStart<rowEnd and colStart<colEnd:

        #top row (left to right)
        for i in range(colStart,colEnd):
                result.append(matrix[rowStart][i])
        rowStart+=1

        #right column (top to bottom)
        for i in range(rowStart,rowEnd):
                result.append(matrix[i][colEnd-1])
        colEnd-=1


        #bottom row (right to left)
        for i in range(colEnd - 1, colStart-1, -1):
                result.append(matrix[rowEnd - 1][i])
        rowEnd -= 1


        #left column (bottom to top)
        for i in range(rowEnd - 1, rowStart-1 , -1):
                result.append(matrix[i][colStart])
        colStart += 1


print(result)














