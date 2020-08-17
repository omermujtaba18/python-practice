import re


def disemvowel(string):
    return re.sub("[aeiouAEIOU]", "", string)


# Test
print(disemvowel("This website is for losers LOL!"))
