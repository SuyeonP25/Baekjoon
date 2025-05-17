N = int(input())
solution = [0]

board = [0] * N
check_row = [False] * N
check_diagonal_up = [False] * (2 * N - 1)
check_diagonal_down = [False] * (2 * N - 1)

def put_queen(i):
    for j in range(N):
        if (not check_row[j]) & (not check_diagonal_up[i + j]) & (not check_diagonal_down[-i + j + N - 1]):
            if i == N - 1:
                solution[0] += 1
            else:
                check_row[j] = check_diagonal_up[i + j] = check_diagonal_down[-i + j + N - 1] = True
                put_queen(i + 1)
                check_row[j] = check_diagonal_up[i + j] = check_diagonal_down[-i + j + N - 1] = False

put_queen(0)
print(solution[0])