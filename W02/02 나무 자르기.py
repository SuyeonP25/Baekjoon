# 나무 자르기

N, M = map(int, input().split())
H = list(map(int, input().split()))

hd, hu = 0, max(H)
target = 0

while hd <= hu:
    hmid = (hd + hu) // 2
    dh_sum = sum(h - hmid for h in H if h > hmid)

    if dh_sum == M:
        target = hmid
        break
    elif dh_sum < M:
        hu = hmid - 1
    else:  # dh_sum > M
        target = hmid
        hd = hmid + 1

print(target)
