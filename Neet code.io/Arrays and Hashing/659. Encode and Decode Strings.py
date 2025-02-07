arr=["neet","code","love","you"]

def encode(arr):
    strs=""
    for elem in arr:
        strs+=elem + "#"

    print(strs)

strs="neet#code#love#you#"

def decode(strs):
    word = strs.split("#")
    word.remove("")
    print(word)

encode(arr)

decode(strs)

