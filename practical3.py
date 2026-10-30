# Count even and odd numbers in an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

even = 0
odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Number of even elements =", even)
print("Number of odd elements =", odd)