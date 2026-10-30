# Move all zeros to the end of an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

result = []

# Add non-zero elements first
for i in range(n):
    if arr[i] != 0:
        result.append(arr[i])

# Add zeros at the end
for i in range(n):
    if arr[i] == 0:
        result.append(arr[i])

print("Array after moving zeros to the end:")

for i in range(n):
    print(result[i], end=" ")