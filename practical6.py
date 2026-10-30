# Removing duplicates from an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

unique = []

for i in range(n):
    if arr[i] not in unique:
        unique.append(arr[i])

print("Array after removing duplicates:")

for i in range(len(unique)):
    print(unique[i], end=" ")