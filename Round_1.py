# Q1. Print an Array
# This function takes an array as input and prints each element one by one


def print_array(arr):

    for element in arr:
        
        print(element)

# First array
array = [2, 5, 3, 8, 7]
print_array(array)

# Second array
Array1 = [20, 50, 30, 80, 70]
print_array(Array1)




# Q2. Print Array Elements After Multiplying by 5
# This function multiplies each element of the array by 5 and prints it


def multiply_and_print_array(arr):

    for element in arr:
        # Multiply each element by 5 and print it
        print(element * 5)

# Input array
array = [1, 2, 3, 4, 5]
multiply_and_print_array(array)




# Q3. Find the Target in the Array
# This function checks whether the target value is present in the array


def find_target_in_array(arr, target):
    # Loop through the array using index
    for i in range(len(arr)):
      
        if arr[i] == target:
          
            print(f'output found at : {i}')
            return
    # If target is not found after full loop
    print("output not found")

# Input array
array = [1, 2, 3, 4, 5]
target = 2
find_target_in_array(array, target)




# Q4. Find Minimum and Maximum in an Array
# This function finds the smallest and largest number in the array


def find_min_and_max(arr):
    # Initialize min and max with the first element of the array
    min_val = arr[0]
    max_val = arr[0]

    # Loop from second element till the end
    for i in range(1, len(arr)):
      
        if arr[i] < min_val:
            min_val = arr[i]
       
        if arr[i] > max_val:
            max_val = arr[i]

    # Print final min and max values
    print(f'Minimum value: {min_val}')
    print(f'Maximum value: {max_val}')

# Input array
array = [3, 1, 4, 1, 5, 9, 2, 6, 5]
find_min_and_max(array)




# Q5. Print All 0’s and 1’s Separately
# This function separates all 0s and 1s into different lists


def print_zeros_then_ones(arr):
    zero = []  
    one = []   

    # Loop through the array
    for i in arr:
        # If element is 0, add to zero list
        if i == 0:
            zero.append(i)
        # Otherwise, add to one list
        else:
            one.append(i)

    # Print separated values
    print("0's:", zero)
    print("1's:", one)
    print(zero, one)

# Input array
array = [0, 1, 0, 1, 1, 0, 0, 1]
print_zeros_then_ones(array)
