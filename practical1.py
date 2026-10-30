# calculate array sum


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

sum = 0

for i in range(n):
    sum = sum + arr[i]

print("Sum of array elements =", sum)