prices =  [10,8,7,5,2]

#finding the minimum value to buy and setting a pointer to it
min_val=max(prices)
ptr=0
for i in range(len(prices)):
    if prices[i]<min_val:
        min_val=prices[i]
        ptr=i
print(min_val,ptr)

#finding the maximum value to sell from pointer to the end of the list
max_val=min(prices)
for i in range(ptr,len(prices)):
    if prices[i] > max_val:
        max_val = prices[i]
print(max_val)

#profit = selling price - cost price
print(max_val - min_val)