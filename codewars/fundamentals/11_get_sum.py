def get_sum(a, b):
    # if b < a:
    #     a, b = b, a

    # sum = 0
    # for i in range(a, b+1):
    #     sum += i

    # return sum

    return sum(range(min(a, b), max(a, b)+1))


print(get_sum(0, -1))
