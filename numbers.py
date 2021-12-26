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