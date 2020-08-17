def create_phone_number(n):
    n = "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
    return n


# Test
print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
