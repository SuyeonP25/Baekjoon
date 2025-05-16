def is_hansu(n):
    if n // 100 - n // 10 % 10 == n // 10 % 10 - n % 10:
        return True
    else:
        return False

N = int(input())

if N < 100 :
    print(N)
else :
    count=99
    for i in range(100, N+1):
        if is_hansu(i):
            count += 1
    print(count)