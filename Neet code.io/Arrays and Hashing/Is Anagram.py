s = "racecar"
t = "carrace"


def isAnagram(s,t):
    hashmapS = {}
    hashmapT = {}

    if len(s)!=len(t):
        return False

    for char in s:
        if char not in hashmapS:
            hashmapS[char] = 1
        else:
            hashmapS[char] += 1
    print(hashmapS)

    for char in t:
        if char not in hashmapT:
            hashmapT[char] = 1
        else:
            hashmapT[char] += 1
    print(hashmapT)

    for char in hashmapS:
        if hashmapS[char] != hashmapT.get(char, 0):
            return False

    return True


print(isAnagram(s,t))