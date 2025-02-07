n=8
count=0

def printing(n,count):
    if count == n:
        return

    print("Misham",count)
    count+=1
    printing(n,count)

printing(n,count)
