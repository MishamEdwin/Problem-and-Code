N=5

res_string="1"  # first line always stays 1

def generate(res_string):
    count=1           # variable to count the occurring
    new_string=""     # string builder to add the count and value

    for i in range(1,len(res_string)): # loop to traverse the string
        if res_string[i] == res_string[i-1]: # if current_value == prev_value
            count+=1                         # increase the count
        else:                                # else
            new_string += str(count) + res_string[i-1]# append the count and the prev_value to the string builder
            count=1               # reset the count variable to 1

    new_string += str(count) + res_string[-1] # append the count and last value to the string builder

    return new_string


for i in range(N):
    print(res_string) # prints the lines
    res_string=generate(res_string) # updating the string using function