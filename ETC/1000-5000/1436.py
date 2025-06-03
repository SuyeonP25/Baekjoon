# 영화감독 숌

import sys

N = int(sys.stdin.readline())

count = 0
num = 665

while count != N:
    num += 1
    if str(num).find('666') != -1:
        count += 1

print(num)
