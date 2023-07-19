# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 8. Write a Python program to traverse a list using for-loop.


my_list = []
num_items = int(input("Enter the number of items in your list: "))
for i in range(num_items):
    item = input("Enter an item: ")
    my_list.append(item)

print("\nPrinting the entered values: ")
for item in my_list:
    print(item)
