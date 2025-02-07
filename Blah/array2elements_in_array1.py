"""There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results."""

strings=[]

queries=[]

result=[]

ns=int(input())

for i in range(ns):
    s=input()
    strings.append(s)

nq=int(input())

for i in range(nq):
    q=input()
    queries.append(q)

print(strings)

print(queries)

for elem in queries:
    if elem in strings:
        count=strings.count(elem)
        result.append(count)
    else:
        result.append(0)
print(result)

for i in result:
    print(i)

"""for i in range(len(queries)):
    if queries[i] in strings:
        result.append(queries[i])
    else:
        result.append(0)

print(result)"""