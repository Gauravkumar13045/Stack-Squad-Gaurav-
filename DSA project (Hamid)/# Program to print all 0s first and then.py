# Program to print all 0s first and then all 1s

arr = list(map(int, input("Enter 0s and 1s: ").split()))

zeros = []
ones = []

for num in arr:
    if num == 0:
        zeros.append(0)
    elif num == 1:
        ones.append(1)

# Print result
for z in zeros:
    print(z, end=" ")

for o in ones:
    print(o, end=" ")
