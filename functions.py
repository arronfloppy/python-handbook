# funtion definition

def hello():
    print('Hello!')

# call the function


hello()

# function with parameters


def hello(name):
    print('Hello ' + name + '!')


# call the function passing un argument


hello("Roger")


""" We call parameters the values accepted by the
function inside the function definition, and
arguments the values we pass to the function
when we call it. It's common to get confused about
this distinction.
 """

"""  An argument can have a default value that's applied if
the argument is not specified: """


def hello(name='my friend'):
    print('Hello ' + name + '!')


hello()


# Hello my friend!

# function with many parameters


def hello(name, age):
    print('Hello ' + name + ', you are ' + str(age))


hello("Roger", 8)


""" Parameters are passed by reference. All types in
Python are objects but some of them are immutable,
including integers, booleans, floats, strings, and
tuples """

# function with return statement


def hello(name):
    if not name:
        return
    print('Hello ' + name + '!')


""" You can return multiple values by using comma
separated values: """


def hello(name):
    print('Hello ' + name + '!')
    return name, 'Roger', 8


""" In this case calling hello('Syd')
the return value is a
tuple containing those
3 values: ('Syd', 'Roger', 8) ."""

print(hello("Syd"))
