# merge sort
N = int(input())
l = [0] * N
tmpl = [0] * N
for i in range(N):
    l[i] = int(input())

def mergesort(l, start, end):
    if start < end:
        mid = (start + end) // 2
        mergesort(l, start, mid)
        mergesort(l, mid + 1, end)

        i = k = start
        j = p = 0

        while i <= mid:
            tmpl[p] = l[i]
            i += 1
            p += 1

        while i <= end and j < p:
            if tmpl[j] <= l[i]:
                l[k] = tmpl[j]
                j += 1
            else:
                l[k] = l[i]
                i += 1
            k += 1

        while j < p:
            l[k] = tmpl[j]
            k += 1
            j += 1

mergesort(l, 0, N - 1)
for i in range(N):
    print(l[i])