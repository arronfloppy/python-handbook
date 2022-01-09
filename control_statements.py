""" When the condition test resolves to True , like in the
above case, its block gets executed.
What is a block? A block is that part that is indented
one level (4 spaces usually) on the right:
The block can be formed by a single line, or multiple
lines as well, and it ends when you move back to the
previous indentation level: """

condition = True
name = "Roger"
if condition:
    print("The condition")
    print("was true")
elif name == "Roger":
    print("Hello Roger")
elif name == "Syd":
    print("Hello Syd")
else:
    print("The condition")
    print("was False")

print("Outside of the if")

""" if and else can also be used in an inline format, """

a = 2
result = 2 if a == 0 else 3
print(result)
# 3
