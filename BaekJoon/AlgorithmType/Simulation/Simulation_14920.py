def recurrence(n, cnt):
    if n == 1:
        return cnt
    if n % 2 == 0:
        return recurrence(n // 2, cnt + 1)
    else:
        return recurrence(3 * n + 1, cnt + 1)
print(recurrence(int(input()), 1))