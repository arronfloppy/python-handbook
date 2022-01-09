from enum import Enum


# Constants
# Python has no way to enforce a variable to be a constant.
# The nearest you can go is to use an enum:


class Constants(Enum):
    WIDTH = 1024
    HEIGHT = 256


# And get to each value using for example
print(Constants.WIDTH.value)
# No one can reassign that value.

# Otherwise if you want to rely on naming conventions, you can adhere to this
#  one: declare variables that
# should never change uppercase:
WIDTH = 1024
# No one will prevent to overwrite this value, and Python
# will not stop it

# Enums

# You can initialize a new enum in this way:


class State(Enum):
    INACTIVE = 0
    ACTIVE = 1


# Once you do so, you can reference State.INACTIVE
# and State.ACTIVE , and they serve as constants

print(State.ACTIVE)
# State.Active
print(State(1))
# State.Active
print(State['ACTIVE'])
# State.Active
print(State.ACTIVE.value)
# 1

# You can list all the possible values of an enum:
print(list(State))

# You can count them:
print(len(State))
