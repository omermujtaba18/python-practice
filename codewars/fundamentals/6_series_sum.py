"""
Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

Rules:
You need to round the answer to 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.

"""


def series_sum(n):
    sum = 0.00
    for i in range(0, n):
        sum += 1.00 / (1 + 3 * float(i))

    return '{:.2f}'.format(sum)


# Test
print(series_sum(2))
