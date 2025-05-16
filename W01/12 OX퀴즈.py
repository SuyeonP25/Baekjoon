N = int(input())
score = 0
n = 0

for i in range(N):
    score = 0
    n = 0
    answer = input()
    for j in range(len(answer)):
        if answer[j] == 'O':
            n += 1
            score += n
        else:
            n = 0
    print(score)