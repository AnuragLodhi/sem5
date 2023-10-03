import sys

stack = []
symbols = ('0', '1')
inp = input("Enter the string: ")
for char in inp:
    if char not in symbols:
        print(f"{char} is not in valid symbols")
        sys.exit(1)
    if len(stack) == 0:
        stack.append(char)
        continue
    if char != stack[-1]:
        stack.pop()
        continue
    stack.append(char)
if len(stack) == 0:
    print("Accepted")
else:
    print("Rejected")