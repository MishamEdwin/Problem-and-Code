inp=[[0,1,1,0,0],
     [0,1,1,0,0],
     [1,1,0,1,1],
     [1,1,0,1,1]]

count=0

rows=len(inp)
cols=len(inp)+1



for i in range(rows):
        for j in range(cols):
                print(inp[i][j],end=" ")
        print()

for i in range(rows-1):
        for j in range(cols-1):
                if((inp[i][j]==1 and inp[i][j+1]==1) and (inp[i+1][j]==1 and inp[i+1][j+1]==1)):
                        count+=1

print()
print(count)