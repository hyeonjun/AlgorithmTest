# b == 1 -> a % c
# b % 2 == 0 -> (a^(b//2)) ^ 2
# b % 2 != 0 -> ((a^(b//2)) ^ 2) * a
def divide(a, b, c):
    if b == 1:
        return a % c
    tmp = divide(a, b//2, c)
    if b % 2 == 0:
        return (tmp ** 2) % c
    else:
        return (tmp ** 2) * a % c
a, b, c = map(int, input().split())
print(divide(a, b, c))