import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
l = []
for i in range(N):
    l.append(int(input()))

for i in range(N):
    for j in range(l[i]//2):
        if is_prime(int(l[i]/2)-j) & is_prime(int(l[i]/2)+j):
            print(f'{int(l[i]/2)-j} {int(l[i]/2)+j}')
            break