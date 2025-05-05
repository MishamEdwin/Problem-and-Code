N = 51
out_space=N//2
in_space=1
fixed_space=N//2

#first
print(" "*fixed_space + "*")

#top
for i in range(N//2):
    print((out_space-1)*" " + "*" + in_space*" " + "*")
    out_space-=1
    in_space+=2

# print(out_space)
# print(in_space)
out_space+=1
in_space-=4

#bottom
for i in range(N//2-1):
    print(out_space*" " + "*" +in_space*" " + "*")
    out_space+=1
    in_space-=2

#last
print(" "*fixed_space + "*")
