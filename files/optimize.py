print("Enter number of statements:")
n = int(input())

code = []
for i in range(n):
    code.append(input())

optimized = []

# Constant Folding
for line in code:
    parts = line.split('=')

    if len(parts) == 2:
        left = parts[0].strip()
        right = parts[1].strip()

        # Check if expression has only numbers
        if right.replace('+', '').replace('-', '').replace('*', '').replace('/', '').isdigit():
            value = eval(right)
            line = left + " = " + str(value)

    optimized.append(line)

# Dead Code Elimination (simple check)
used = set()

for line in optimized:
    if '=' in line:
        right = line.split('=')[1]
        for char in right:
            if char.isalpha():
                used.add(char)

final_code = []

for line in optimized:
    if '=' in line:
        left = line.split('=')[0].strip()
        if left in used or line == optimized[-1]:
            final_code.append(line)
    else:
        final_code.append(line)

# Output
print("\nOptimized Code:\n")
for line in final_code:
    print(line)