# 알파벳 찾기

S = input()
for i in range(26):
    print(S.find(chr(97+i)), end=' ')