# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 2. Write a Python program to calculate the sum of all positive and negative numbers from the list of N numbers.


n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter an element: ")))

positive_sum = 0
negative_sum = 0

for num in lst:
    if num >= 0:
        positive_sum += num
    else:
        negative_sum += num

print(f"Sum of positive numbers: {positive_sum}")
print(f"Sum of negative numbers: {negative_sum}")
