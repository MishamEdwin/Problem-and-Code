matrix=[[1 ,2, 3, 4],
        [12,13,14,5],
        [11,16,15,6],
        [10 ,9 ,8,7]]


# declaring 4 variables to set boundaries
row_start=0
col_start=0
row_end=len(matrix)
col_end=len(matrix[0])

result=[]
while row_start<row_end and col_start<col_end:

    #top (left to right) so loop the columns
    for i in range(col_start,col_end):
        print(matrix[row_start][i],end=" ")
    row_start+=1

    #right (up to down) so loop through the rows
    for i in range(row_start,row_end):
        print(matrix[i][col_end-1],end=" ")
    col_end-=1

    #bottom (right to left) so loop through the columns
    for i in range(col_end-1,col_start-1,-1):
        print(matrix[row_end-1][i],end=" ")
    row_end-=1

    #left (down to up) so loop through the rows
    for i in range(row_end-1,row_start-1,-1):
        print(matrix[i][col_start],end=" ")
    col_start+=1

