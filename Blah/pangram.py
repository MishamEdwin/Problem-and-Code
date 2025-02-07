s="We promptly judged antique ivory buckles for the prize"

lower=[chr(i) for i in range(97,123)]
upper=[chr(i) for i in range(65,91)]

new_string=s.lower()

is_pangram=True

for char in lower:
    if char not in new_string:
        is_pangram=False
        break

if is_pangram:
    print("pangram")
else:
    print("not pangram")
