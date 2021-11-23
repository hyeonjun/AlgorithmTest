n = sorted(input(), reverse=True)
s = sum(list(map(int, n)))
if s % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(''.join(n))