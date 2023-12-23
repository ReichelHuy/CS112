L1, R1, L2, R2 = map(int, input().split())
Lmax = max(L1, L2)
Rmin = min(R1, R2)
ans = Rmin - Lmax
print(ans if ans >=0 else 0)