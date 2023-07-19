# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 5. Write a Python program to calculate the simple interest.


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100

print(f"Simple interest: {simple_interest:.2f}")
