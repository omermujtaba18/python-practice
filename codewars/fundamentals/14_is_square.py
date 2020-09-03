import math


def is_square(n):

    return n >= 0 and math.sqrt(n) % 1 == 0


print(is_square(0))

# print(math.sqrt(0))
