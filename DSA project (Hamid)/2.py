# Program to multiply each element of an array by 5 and print it

arr = list(map(int, input("Enter numbers separated by space: ").split()))

for num in arr:
    print(num * 5, end=" ")
