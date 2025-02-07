s="zohocorporation"
mid=len(s)//2
print(mid)
new=s.split(s[mid])

print(new)
first=new[0]
second=new[1]
center=s[len(s)//2]

print(first,center,second)

start=0
end=-1
fblank=0
sblank=len(s)-2
white=chr(32)

for i in range(len(first)):
    print(fblank*white,first[start],sblank*white,second[end])
    start+=1
    end-=1
    fblank+=1
    sblank-=2
lengthfirst=len(first)+1
print(white*lengthfirst,center)

nstart=0
nend=-1
nfblank=len(first)-1
nsblank=1
for i in range(len(first)):
    print(nfblank*white,first[nend],nsblank*white,second[nstart])
    nend-=1
    nstart+=1
    nfblank-=1
    nsblank+=2