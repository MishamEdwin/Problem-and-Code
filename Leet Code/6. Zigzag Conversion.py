s="PAYPALISHIRING"
n=3

if n==1:
    print(s)

outputstr=""

for rows in range(n):
    #formula for 1st and last rows
    increment=(n-1)*2
    for i in range(rows,len(s),increment):
        outputstr+=s[i]

        #formula for middle rpws
        if(rows>0 and rows<n-1 and
           i+increment-2*rows < len(s)):
            outputstr+=s[i+increment-2*rows]

print(outputstr)





























