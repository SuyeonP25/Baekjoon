A, B, V = map(int, input().split())

daily = A-B
normalday = (V-A)//daily
if (V-A)-daily*normalday != 0:
    print(normalday+2)
else:
    print(normalday+1)