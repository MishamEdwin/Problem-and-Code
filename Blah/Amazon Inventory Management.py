def maximize_similarity(inv1, inv2):
    n = len(inv1)
    matches = 0

    # Step 1: Count initial matches
    for i in range(n):
        if inv1[i] == inv2[i]:
            matches += 1

    # Step 2: Try to balance inv1 with inv2
    excess = 0
    deficit = 0

    # Calculate how much extra or short inv1 is compared to inv2
    for i in range(n):
        if inv1[i] > inv2[i]:
            excess += inv1[i] - inv2[i]
        elif inv1[i] < inv2[i]:
            deficit += inv2[i] - inv1[i]

    # Step 3: Try to balance the excess and deficit to maximize matches
    possible_operations = min(excess, deficit)
    matches += possible_operations

    return matches


# Example usage:
inv1 = [2,4,1]
inv2 = [1,2,3]
result = maximize_similarity(inv1, inv2)
print("Maximum similarity:", result)
