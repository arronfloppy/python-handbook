# A list can hold values of different types:
items = ["Roger", 1, "Syd", True]
print(items)

print("Roger" in items)
# True

# A list can also be defined as empty:
items2 = []

# You can reference the items in a list by their index, starting from zero:
print(items[0])
# "Roger"
print(items[1])
# 1
print(items[3])
# True

# Using the same notation you can change the value stored at a specific index:
items[0] = "Roger 2"
print(items[0])

print(len(items))
# 4 items

# can't do this
# items[4] = "Toto"

# You can also use the index() method:
print(items.index(0))
# "Roger"
