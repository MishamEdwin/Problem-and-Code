# Get input from user
n = int(input("Enter a number (n): "))

# Create a list of numbers from 1 to n
numbers = list(range(1, n + 1))


# Function to find and display all combinations that sum up to n
def find_combinations(numbers, target_sum):
    def find_combos(current, start, target):
        # Base case: if target is zero, we have a valid combination
        if target == 0:
            print(" + ".join(map(str, current)))
            return
        # Iterate over the numbers starting from index 'start'
        for i in range(start, len(numbers)):
            if numbers[i] > target:
                continue
            # Recur with the current number included
            find_combos(current + [numbers[i]], i + 1, target - numbers[i])

    find_combos([], 0, target_sum)


# Find and display the combinations
find_combinations(numbers, n)
