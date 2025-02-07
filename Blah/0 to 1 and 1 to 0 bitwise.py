n=int(input())
q=[]
for i in range(n):
    elem=int(input())
    q.append(elem)



def conversion(num):
    binary_rep = ""
    for i in range(31,-1,-1):
        num2=(num>>i)&1
        binary_rep +=str(num2)
    inversion(binary_rep)


def inversion(binary_rep):
    inversion_rep="".join("1" if bit == "0" else "0" for bit in binary_rep)
    inversion_calc=int(inversion_rep,2)
    print(inversion_calc)

for nums in q:
    bitnum=nums
    conversion(bitnum)

