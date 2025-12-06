# Program to find minimum and maximum elements in an array

arr = list(map(int, input("Enter array elements: ").split()))

minimum = arr[0]
maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Min =", minimum)
print("Max =", maximum)
