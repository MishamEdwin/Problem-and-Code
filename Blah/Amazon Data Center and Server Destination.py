n=3
center=[1,2,2]
destination=[5,2,4]

center.sort()
destination.sort()

ans=[]
for i in range(n):
    res=abs(center[i]-destination[i])
    ans.append(res)

print(ans,sum(ans))