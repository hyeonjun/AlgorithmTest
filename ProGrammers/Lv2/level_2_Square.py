def solution(w,h):
    def gcd(n,m):
        while m > 0:
            n, m = m, n%m
        return n
    if h > w:
        w, h = h, w
    gN = gcd(w, h)
    return (w * h) - (w + h - gN)

print(solution(8, 12))