# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 9. Write a Python program to calculate:  S = 1 + x + x^2 + x^3 + ... + x^n


x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

sum = 0
for i in range(n+1):
    term = x ** i
    sum += term

print("The sum is:", sum)
