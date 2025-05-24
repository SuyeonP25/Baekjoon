# FizzBuzz

import sys

l = list()
for _ in range(3):
    l.append(sys.stdin.readline())

ans = 0
for i in range(3):
    if l[i].find('z') == -1:
        ans = int(l[i]) + 3 - i
        break

if ans % 15 == 0:
    print('FizzBuzz')
elif ans % 3 == 0:
    print('Fizz')
elif ans % 5 == 0:
    print('Buzz')
else:
    print(ans)
