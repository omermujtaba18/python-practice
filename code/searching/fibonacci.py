"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""


def get_fib(position):

    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)


# get_fib(3)
#     get_fib(2)          +        get_fib(1)
#         get_fib(1) + get_fib(0)    +   1
#             1      +     0
#                   1         +       1

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
print(get_fib(3))
