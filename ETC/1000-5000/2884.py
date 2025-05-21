# 알람 시계

H, M = map(int, input().split())

if M < 45:
    H = (H + 23) % 24

print(f'{H} {(M + 15) % 60}')
