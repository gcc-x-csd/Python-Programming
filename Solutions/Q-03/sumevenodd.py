# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 3. Write a Python program to calculate the sum of all even and odd numbers from the list of N numbers.


n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter an element: ")))

even_sum = 0
odd_sum = 0

for num in lst:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"Sum of even numbers: {even_sum}")
print(f"Sum of odd numbers: {odd_sum}")
