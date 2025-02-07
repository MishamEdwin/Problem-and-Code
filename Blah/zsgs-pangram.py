lowercase=[]
for i in range(97,123):
    lowercase.append(chr(i))

print(lowercase)

inp="abcdefghiJklMNopqrsTUvWxyz"
string=inp.lower()

print(len(string))

is_pangram=True

for elem in lowercase:
    if elem not in string:
        is_pangram=False
        break

if is_pangram:
    print("1")
else:
    print("0")