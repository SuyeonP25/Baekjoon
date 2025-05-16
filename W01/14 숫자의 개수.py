A, B, C = int(input()), int(input()), int(input())
m = str(A*B*C)
count = 0

for i in range(10):
    count=0
    for j in range(len(m)):
        if str(i) == m[j]:
            count += 1
    print(count)