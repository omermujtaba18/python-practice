def accum(s):
    value = ""
    for i in range(0, len(s)):
        for j in range(0, i+1):
            value += s[i].upper() if j == 0 else s[i].lower()
        value += "-"
    return value[:-1]


# Test
print(accum("ZpglnRxqenU"))
