# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 1. Write a Python program to calculate the factorial of an integer number.


num = int(input("Enter a number: "))
factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"Factorial of {num} is {factorial}.")
