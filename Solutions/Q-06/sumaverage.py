# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 6. Write a Python program to find the sum and average from the list of N numbers.


n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter an element: ")))

sum_lst = sum(lst)
average = sum_lst / n

print(f"Sum of the list: {sum_lst}")
print(f"Average of the list: {average:.2f}")
