# Hashing

L = int(input())
S = input()
h = 0

for i in range(L):
    h += (ord(S[i]) - 96) * 31 ** i

h = h % 1234567891
print(h)
