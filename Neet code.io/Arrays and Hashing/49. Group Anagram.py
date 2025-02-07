strs = ["act","pots","tops","cat","stop","hat"]
dictionary={}

for words in strs:
    sorted_words=sorted(words)
    key=tuple(sorted_words)

    if key not in dictionary:
        dictionary[key]=[words]
    else:
        dictionary[key].append(words)

print(dictionary)
print(dictionary.values())