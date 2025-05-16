C = int(input())
avg = 0

for i in range(C):
    avg = 0
    student = 0
    l = list(map(int, input().split()))
    for j in range(l[0]):
        avg+=l[j+1]
    avg/=l[0]
    for j in range(l[0]):
        if l[j+1]>avg:
            student += 1
    print(f'{student/l[0] * 100:.3f}%')