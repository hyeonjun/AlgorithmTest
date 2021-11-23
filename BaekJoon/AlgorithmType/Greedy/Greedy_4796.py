idx = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    q, r = divmod(v, p)
    result = q*l
    result += min(r, l)
    print('Case {0}: {1}'.format(idx, result))
    idx += 1
