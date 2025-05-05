n=14341
temp=n
rev=0

while temp>0:
    #  mul rev*10 to increase the unit position(O,T,H,TH...) for each number to add
    rev= rev*10 + temp%10
    temp//=10

if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")





