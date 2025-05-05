s="A&x#"
new_s=list(s)

top=0
bottom=len(new_s)-1

while top < bottom :
    if new_s[top].isalpha() and new_s[bottom].isalpha():
        new_s[top],new_s[bottom]=new_s[bottom],new_s[top]
        top+=1
        bottom-=1


    elif not new_s[top].isalpha() and new_s[bottom].isalpha():
        top+=1


    elif new_s[top].isalpha() and (not new_s[bottom].isalpha()):
        bottom-=1

    else:
        top+=1
        bottom-=1

print("".join(new_s))
