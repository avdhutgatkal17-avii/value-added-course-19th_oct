#find largest to smallest numbers

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

largest = arr[0]
second_largest = arr[0]
smallest = arr[0]
second_smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]

    elif arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]

    if arr[i] < smallest:
        second_smallest = smallest
        smallest = arr[i]

    elif arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]

print("Largest element =", largest)
print("Second largest element =", second_largest)
print("Smallest element =", smallest)
print("Second smallest element =", second_smallest)
