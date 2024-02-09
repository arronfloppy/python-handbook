# Numbers in Python can be of 3 types: int , float and complex

# Integer numbers
# Integer numbers are represented using the int class

age = 8
age = int(8)
type(age) == int
# True

# Floating point numbers
# Floating point numbers (fractions) are of type float

fraction = 0.1
fraction = float(0.1)
type(fraction) == float

# Complex numbers
# Complex numbers are of type complex

complexNumber = 2+3j
complexNumber = complex(2, 3)
type(complexNumber) == complex

complexNumber.real
# 2.0
complexNumber.imag
# 3.0

# Arithmetic operations on numbers
1 + 1
# 2
2 - 1
# 1
2 * 2
# 4
4 / 2
# 2
4 % 3
# 1
4 ** 2
# 16
4 // 3
# 1

age = 8
age += 1

# built-in functions

# abs() returns the absolute value of a number.
# round() given a number, returns its value rounded to the nearest integer:

round(0.12)
# 0

round(0.51)
# 1


