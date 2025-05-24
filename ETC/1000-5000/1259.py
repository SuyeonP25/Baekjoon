# 팰린드롬수

while True:
    S = input()
    if S == "0":
        break
    isP = True
    for i in range(len(S) // 2):
        if S[i] != S[-i - 1]:
            isP = False
            break
    if isP:
        print("yes")
    else:
        print("no")
