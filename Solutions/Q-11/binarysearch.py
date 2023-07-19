# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 11. Write a Python program to implement binary search.


# Define a function to perform binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Take user input for the list of numbers and target value
arr = list(map(int, input("Enter a sorted list of numbers, separated by spaces: ").split()))
target = int(input("Enter the target value: "))

# Call the binary search function and print the result to the console
result = binary_search(arr, target)
if result == -1:
    print("\nTarget value not found in list")
else:
    print("\nTarget value found at index", result)
