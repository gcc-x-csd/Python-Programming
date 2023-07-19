# By - Kaustav Purkayastha ( Gurucharan University, Silchar - @ Department of Computer Science )

# 10. Write a Python program to implement stack using list.


# Define an empty list to represent the stack
stack = []

# Define a function to push an element onto the stack
def push(element):
    stack.append(element)

# Define a function to pop an element off the stack
def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        return None

# Take user inputs to push elements onto the stack
num_items = int(input("Enter the number of items to push onto the stack: "))
for i in range(num_items):
    item = input("Enter an item to push onto the stack: ")
    push(item)

# Pop elements off the stack and print them to the console
print("\nThe Entered Stack is: ")
while True:
    item = pop()
    if item is not None:
        print(item)
    else:
        break
