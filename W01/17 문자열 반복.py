T = int(input())

for i in range(T):
    N = input().split()
    for j in range(len(N[1])):
        for k in range(int(N[0])):
            print(f'{N[1][j]}', end='')
    print()