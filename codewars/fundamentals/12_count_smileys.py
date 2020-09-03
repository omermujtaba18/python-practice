def count_smileys(arr):
    sum = 0
    for s in arr:
        if s[0] in [':', ';'] and s[-1] in [')', 'D']:
            if len(s) > 2:
                if s[1] in ['-', '~']:
                    sum += 1
            else:
                sum += 1
    return sum


print(count_smileys([':D', ':~)', ';~D', ':)']))
