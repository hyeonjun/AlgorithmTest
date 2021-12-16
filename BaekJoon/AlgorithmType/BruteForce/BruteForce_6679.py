def cal(n, base):
    result = 0
    while n > 0:
        result += n % base
        n = n // base
    return result

for i in range(1000, 10000):
    de, do, hx = cal(i, 10), cal(i, 12), cal(i, 16)
    if de == do == hx:
        print(i)