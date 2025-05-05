s = list("OXOX")

n=len(s)

moves=0

for i in range(n):
    if (s[i]=="X"):
        s[i]="O"
        moves+=1
        if (i+1<n):
            s[i+1]="O"
        if (i+2<n):
            s[i+2]="O"

print(moves)
