memory = [3, 4, 5]
new_memory = [0] * len(memory)

# Sort memory in reverse
memory.sort(reverse=True)

for i in range(len(memory)):
    if i == 0:
        new_memory[0] = memory[0]
    else:
        # Add the current memory value to the previous new_memory value
        new_memory[i] = new_memory[i - 1] + memory[i]

print(new_memory)
