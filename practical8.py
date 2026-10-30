# 1. Plus Pattern

n = 7

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()


# 2. Square Border Pattern

n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()


# 3. Diamond Pattern

n = 7

for i in range(n):
    for j in range(n):
        if abs(i - n // 2) + abs(j - n // 2) == n // 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print()


# 4. Number Pyramid

n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

print()


# 5. 0 and 1 Pattern

n = 5

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()