# The basics of working with python
# select code in VSCode and run with shift + enter

# statements
name = "Roger"
print(name)
print(1+1)

# multiple statements, flake8 linter is unhappy
name = "Roger"; print(name)

# this is a commented line
# flake8 linter is unhappy about the following line
name = "Roger"; print(name)  # this is an inline comment

# Datatypes

# String datatype
name = "Roger"
type(name) == str

name = "Roger"
isinstance(name, str)

# Numbers
age = 1
type(age) == int

fraction = 0.1
type(fraction) == float

# Casting
age = int("20")
# 20
print(age)
type(age) == int

age = str(20)
print(age)
type(age) == str

fraction = 0.1
intFraction = int(fraction)
# 0
print(intFraction)

# Operators
# Arithmetic operators
# 2
1 + 1
# 1
2 - 1
# 4
2 * 2
# 2
4 / 2
# 1
4 % 3
# 16
4 ** 2
# 1
4 // 3

# String concatenation
print("Roger " + "is a good dog")

# We can combine the assignment operator with arithmetic operators
# += -= *= /= %= ..and so on
age = 8
age += 1
# age is now 9
print(age)
age /= 2
# age is now 4.5
print(age)

# Comparison operators
# You can use those operators to get a boolean value ( True or False )
# depending on the result
a = 1
b = 2
# False
a == b

# True
a != b

# False
a > b

# True
a <= b

# Boolean operators
# Python gives us the following boolean operators: not and or
# Pay attention of this!!!

# or used in an expression returns the value of the first operand that is not a
# falsy value ( False , 0 ,'' , [] ..). Otherwise it returns the last operand
# if x is false, then y, else x .

# 1
print(0 or 1)

# 'hey'
print(False or 'hey')

# 'hi'
print('hi' or 'hey')

# 'False'
print([] or False)

# '[]'
print(False or [])

# and only evaluates the second argument if the first one is true. So if the
# first argument is falsy ( False ,0 , '' , [] ..), it returns that argument.
# Otherwise it evaluates the second argument:
# if x is false, then x, else y

# 0
print(0 and 1)

# 0
print(1 and 0)

# False
print(False and 'hey')

# 'hey'
print('hi' and 'hey')

# []
print([] and False)

# False
print(False and [])

# []
print(True and [])

# Bitwise operators
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation

# is and in operators
# is == identity operator operator. It is used to compare two objects
# and returns true if both are the same object.
# in == membership operator, Is used to tell if a value is contained in a list,
# or another sequence


# ternary operator
# <result_if_true> if <condition> else <result_if_false>


def is_adult1(age):
    """instead of writting"""
    if age > 18:
        return True
    else:
        return False


def is_adult2(age):
    return True if age > 18 else False


print(is_adult1(20))
print(is_adult2(20))


def is_adult3(age):
    """instead of writting"""
    if age > 18:
        return "adult"
    else:
        return "child"


def is_adult4(age):
    return "adult" if age > 18 else "child"


print(is_adult3(20))
print(is_adult4(20))
