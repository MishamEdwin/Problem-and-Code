arr=[5, 11, 10, 20, 9, 16, 23]
facts={}

def factors(num):
    f=[]
    for i in range(1,num+1):
        if num%i == 0:
            f.append(i)
    return len(f)

for elem in arr:
    a=factors(elem)
    facts[elem]=a

print(facts)

sorted_facts=sorted(facts.items(),reverse=True,key=lambda x:x[1])
print(sorted_facts)

for k,v in sorted_facts:
    print(k,end=" ")