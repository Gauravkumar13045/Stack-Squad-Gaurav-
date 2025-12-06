#array:
"""Q1. Print an Array
Write a program that takes an array as input and prints all its elements."""

def print_array(arr):
    for element in arr:
        print(element)
# Example usage:
array = [1, 2, 3, 4, 5]
print_array(array)


Array1 = [10, 20, 30, 40, 50]
print_array(Array1)


"""2.Print Array Elements After Multiplying by 5
Write a program that multiplies every element in the given array by 5 and prints the updated array"""

def multiply_and_print_array(arr):
    for element in arr:
        print(element * 5)
# Example usage:
array = [1, 2, 3, 4, 5]
multiply_and_print_array(array)


"""Q3. Find the Target in the Array
Write a program to find whether a given target value exists in the array or not.
"""

def find_target_in_array(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            print(f'output found at : {i}')
            return
    print("output not found")

array = [1, 2, 3, 4, 5]
target = 2
find_target_in_array(array,target)


"""Q4. Find Minimum and Maximum in an Array
Write a program to find the smallest (min) and largest (max) number in the array"""

def find_min_and_max(arr):
    # Initialize min and max with the first element of the array

    min_val = arr[0]
    max_val = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        if arr[i] > max_val:
            max_val = arr[i]
    print(f'Minimum value: {min_val}')
    print(f'Maximum value: {max_val}')
    # Example :
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
find_min_and_max(array)



"""Q5. Print All 0’s and 1’s Separately
Given an array containing 0s and 1s, print all the 0s first and then all the 1s"""

def print_zeros_then_ones(arr):
    zero = []
    one = []
    for i in arr:
        if i == 0:
            zero.append(i)
        else:
            one.append(i)
    print("0's:", zero)
    print("1's:", one)
    print(zero, one)
# Example usage:
array = [0, 1, 0, 1, 1, 0, 0, 1]
print_zeros_then_ones(array)

arr = [1, 0, 1, 0, 0, 1]
print("Output:", end=" ")

# Print all the 0s
for num in arr:
    if num == 0:
        print(0, end=" ")

# Print all the 1s
for num in arr:
    if num == 1:
        print(1, end=" ")


