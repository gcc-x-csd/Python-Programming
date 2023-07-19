# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 7. Write a Python program to count the no. of occurrences of an element in a list using function.


def count_occurrences(lst, element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count

n = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter an element: ")))

element = int(input("Enter the element whose occurrences you want to count: "))

occurrences = count_occurrences(lst, element)

print(f"The number of occurrences of {element} in the list is {occurrences}.")
