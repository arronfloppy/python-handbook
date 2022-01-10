# A list can hold values of different types:
items = ["Roger", 1, "Syd", True]
print(items)

print("Roger" in items)
# True

# A list can also be defined as empty:
items2 = []

items = ["Roger", "Glov", "Syd", "Bar"]

# You can reference the items in a list by their index, starting from zero:
print(items[0])
# "Roger"
print(items[1])
# 1
print(items[3])
# True

# Using the same notation you can change the value stored at a specific index:
items[0] = "Ian"
print(items[0])

print(len(items))
# 4 items

# can't do this
# items[4] = "Toto"

# You can also use the index() method to find the index of a value:
print(items.index("Ian"))
# 0

# You can add items to the list by using a list append() method:
items.append("Test")

# or the extend() method:
items.extend(["test1", "test2"])
# or +=
items += ["test3"]
print(items)

# Remove an item using the remove() method:
items.remove("Test")

# To add an item in the middle of a list, at a specific index,
# use the insert() method:
items.insert(1, "Test")
# add "Test" at index 1
print(items)

# To add multiple items at a specific index, you need to use slices:
items[1:1] = ["Test1", "Test2"]

# Sort a list using the sort() method:
items.sort()
print(items)

""" Tip: sort() will only work if the list holds values that
can be compared. Strings and integers for
example can't be compared, and you'll get an
error like TypeError: '<' not supported between
instances of 'int' and 'str' if you try. """

""" The sort() methods orders uppercase letters first,
then lowercased letters. To fix this, use: """
items.sort(key=str.lower)

""" Sorting modifies the original list content. To avoid that,
you can copy the list content using """
itemscopy = items[:]

""" or use the sorted() global function: """
print(sorted(items, key=str.lower))
""" that will return a new list, sorted, instead of modifying
the original list. """
