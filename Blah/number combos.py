def find_combinations(n, start=1, current_combination=[]):
    if n == 0:
        print('+'.join(map(str, current_combination)))
        return
    for i in range(start, n + 1):
        if i <= n:
            find_combinations(n - i, i + 1, current_combination + [i])

# Input value
n = 10

# Find all combinations
find_combinations(n)
