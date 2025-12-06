# Program to print all elements of an array

# take input from user
arr = list(map(int, input("Enter numbers separated by space: ").split()))

# print elements
for num in arr:
    print(num, end=" ")
