from collections import Counter

n = int(input())
l = [int(i) for i in str(n)]

duplicate_items = [i for i in l if l.count(i) > 1]
counts = dict(Counter(l))
duplicates = {key: value for key, value in counts.items() if value > 1}

def include_zero(l):
    if 0 in l[:]:
        return('True')
    else:
        return('False')

def include_two(a):
    if 2 in a and a.get(2) == 2:
        return('True')
    else:
        return('False')

def include_pair_number(l):
    index = 0
    while index < len(l)-1:
        if l[index + 1] - l[index] == 1:
            return('True')
        else:
            index += 1
    else:
        return('False')

print(include_zero(l))
print(include_two(duplicates))
print(include_pair_number(l))