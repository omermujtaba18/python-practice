def open_or_senior(data):
    # list_membership = []
    # for i in data:
    #     if i[0] > 54 and i[1] > 7:
    #         list_membership.append('Senior')
    #     else:
    #         list_membership.append('Open')
    # return list_membership

    return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]


# ['Open', 'Senior', 'Open', 'Senior'])
print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
