temperatures = [30, 38, 30, 36, 35, 40, 28]
result = [0] * len(temperatures)

for i in range(len(temperatures)):
    for j in range(i + 1, len(temperatures)):
        if temperatures[j] > temperatures[i]:
            result[i] = j - i # difference in days like R - L
            break  # Stop after finding the first warmer day

print(result)
