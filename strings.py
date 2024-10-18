

# assign string to a variable
name = "Roger"

# concatenate strings
phrase = "Roger " + " is a good dog"

# append to a string
name = "Roger"
name += " is a good dog"
print(name)

# convert a number to astring
str(8)

print("Roger is " + str(8) + " years old")

# A string can be multi-line when defined with a special
# syntax, enclosing the string in a set of 3 quotes:
print("""Roger is
8
years old
""")

# double quotes, or single quotes
print('''
Roger is
8
years old
''')

# string built-in methods
# isalpha() isalnum() lower() islower() upper() isupper() title() startsswith()
# strip() endswith() replace() split() ...
name = 'two words'
res = name.split(' ')
print(res)
name = 'oneword'
res = name.split(' ')
print(res)

# None of those methods alter the original string. They return a new,
# modified string instead. For example:
name = "Roger"
print(name.lower())
# "roger"
print(name)
# "Roger"

# finding a substring
name = "Roger Roger"
print(name)
print(name.find("ger"))
# 2
# reverse find a substring
print(name.rfind("ger"))
# 8
print(name.rfind("Syd"))
# -1

# find a substring with index
print(name.index("ger"))
# 2

try:
    print(name.index("syd"))
except ValueError:
    print("exception throwed")


# global functions for strings ex: len
name = "Roger"
print(len(name))

# in operator
name = "Roger"
print("ger" in name)
# True

# escape string
name = "Ro\"ger"

# get its characters using square brackets to get a specific item,
# given its index, starting
# from 0:
name = "Roger"
name[0]
# 'R'
name[1]
# 'o'
name[2]
# 'g'

# Using a negative number will start counting from the end:
name = "Roger"
name[-1]
# "r"

# You can also use a range, using what we call slicing:
name = "Roger"
assert (name[1:3] == "og")
assert (name[2:4] == "ge")
assert (name[:2] == "Ro")
assert (name[2:] == "ger")
assert (name[:10] == "Roger")
# "ger"
