# 잃어버린 괄호

import sys

I = sys.stdin.readline().strip()

res = 0
sum = 0
tmp = 0
mod = '+'

for i in I:
    if i.isdigit():
        tmp *= 10
        tmp += int(i)
    elif i == '-':
        if mod == '+':
            res += tmp
            mod = '-'
        else:
            sum += tmp
        tmp = 0
    else:
        if mod == '+':
            res += tmp
        else:
            sum += tmp
        tmp = 0

if mod == '+':
    res += tmp
else:
    sum += tmp
res -= sum

print(res)
