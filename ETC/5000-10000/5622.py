# 다이얼

S = input()
total = 0

for c in S:
    if ord(c) < 83:
        total += (ord(c) - 56) // 3
    else:
        if c == 'S':
            total += 8
        elif c == 'T' or c == 'U' or c == 'V':
            total += 9
        else:
            total += 10

print(total)
