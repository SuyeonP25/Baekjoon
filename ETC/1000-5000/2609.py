# 최대공약수와 최소공배수

def gcd(a, b) -> int:
    if not a % b:
        return b
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())

if N < M:
    gcdnm = gcd(M, N)
else:
    gcdnm = gcd(N, M)

print(gcdnm)
print(N * M // gcdnm)
