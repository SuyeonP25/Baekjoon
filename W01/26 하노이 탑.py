def hanoi_count(n):
    if n == 1:
        return 1
    else:
        return 2*hanoi_count(n-1)+1

def hanoi_procedure(steps, start, end):
    if steps == 1:
        print(f'{start} {end}')
    else :
        hanoi_procedure(steps-1, start, 6-(start+end))
        print(f'{start} {end}')
        hanoi_procedure(steps-1, 6-(start+end), end)

N = int(input())
print(hanoi_count(N))
if N<=20:
    hanoi_procedure(N, 1, 3)