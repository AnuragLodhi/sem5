stack = []
inp = input("Enter the string: ")
for char in inp:
    if len(stack) == 0:
        stack.append(char)
    else:
        stack.pop()
if len(stack) == 0:
    print("Accepted")
else:
    print("Rejected")