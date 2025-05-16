import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
l = list(map(int, input().split()))
count = 0

for i in range(len(l)):
    if is_prime(l[i]):
        count += 1

print(count)