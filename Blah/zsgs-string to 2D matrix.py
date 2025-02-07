#6x5 matrix
inp="WELCOMETOZOHOOFGRADUATESTUDIES"
find="ATE"

alphs=[]
matrix=[]

for chars in inp:
    alphs.append(chars)

rows=6
cols=5
ptr=0

#construction of matrix
for i in range(rows):
    arr=[]
    for j in range(cols):
        arr.append(alphs[ptr])
        ptr+=1
    matrix.append(arr)

#printing the matrix
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j],end=" ")
    print()


#finding the position of the 2nd string
for i in range(rows):
    for j in range(cols):
        if((matrix[i][j]==find[0]) and (matrix[i][j+1]==find[1]) and (matrix[i][j+2]==find[2])):
            print("Start index:","<",i,",",j,">")
            print("End index:", "<", i, ",", j+2, ">")