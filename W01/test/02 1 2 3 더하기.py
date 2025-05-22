# 1, 2, 3 더하기

def divide(n) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return 1
    else:
        return divide(n - 3) + divide(n - 2) + divide(n - 1)

T = int(input())
for _ in range(T):
    n = int(input())
    print(divide(n))

# 주어진 수를 1,2,3의 합으로 나타내는 unique한 가짓수를 구하는 코드

# def divide(n, d) -> int:
#     if n < 0:
#         return 0
#     elif d == 1:
#         return 1
#     else:
#         return divide(n, d - 1) + divide(n - d, d)
#
# T = int(input())
#
# for _ in range(T):
#     n = int(input())
#     print(divide(n, 3))
