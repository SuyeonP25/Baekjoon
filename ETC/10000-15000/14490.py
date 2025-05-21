# 백대열

N, M = map(int, input().split(':'))
if N < M:
    A, B = M, N
else:
    A, B = N, M

def GCD(a, b) -> int:
    while b != 0:
        a, b = b, a % b
    return a

gcd = GCD(A, B)

print(f'{N // gcd}:{M // gcd}')
