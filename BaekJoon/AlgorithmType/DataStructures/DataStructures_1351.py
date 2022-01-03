n, p, q = map(int, input().split())
seq = {0:1}
def dp(i):
    if i in seq:
        return seq[i]
    seq[i] = dp(i//p) + dp(i//q)
    return seq[i]
print(dp(n))