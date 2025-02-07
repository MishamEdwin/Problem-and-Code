string1="test123string"
string2="123"

n=len(string1)
m= len(string2)
i=0
j=0
count=0
char=[]

while(i<n):
    if(string1[i]!=string2[j]):
        i+=1

    elif(string1[i]==string2[j]):
        count+=1
        char.append(string1[i])
        i+=1
        j+=1
        if j==m:
            j=0

print("count = ",count)
print(char)
