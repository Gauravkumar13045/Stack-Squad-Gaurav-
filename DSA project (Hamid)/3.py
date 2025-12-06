# Program to find target in an array

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter target value: "))

found = False

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        found = True
        break

if not found:
    print("Not found")
