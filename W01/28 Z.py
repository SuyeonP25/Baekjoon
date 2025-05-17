def Z(N:int, r:int, c:int):
    if N == 1:
        if not r:
            if not c:
                return 0
            else:
                return 1
        else:
            if not c:
                return 2
            else:
                return 3
    else:
        if r<2**(N-1):
            if c<2**(N-1):
                return 0*(2**(N-1))**2+Z(N-1,r,c)
            else:
                return 1*(2**(N-1))**2+Z(N-1,r,c-2**(N-1))
        else:
            if c<2**(N-1):
                return 2*(2**(N-1))**2+Z(N-1,r-2**(N-1),c)
            else:
                return 3*(2**(N-1))**2+Z(N-1,r-2**(N-1),c-2**(N-1))

N, r, c = map(int, input().split())
print(Z(N,r,c))