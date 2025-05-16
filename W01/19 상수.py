A, B = map(int, input().split())
newA = A%10*100 + A%100//10*10 + A//100
newB = B%10*100 + B%100//10*10 + B//100
print(max(newA, newB))