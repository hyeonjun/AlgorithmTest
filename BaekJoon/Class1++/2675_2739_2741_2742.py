# 2675
for _ in range(int(input())):
    r, s = input().split()
    p = ""
    for s_ in s:
        p += s_ * int(r)
    print(p)

# 2739
n = int(input())
for i in range(9):
    print('{0} * {1} = {2}'.format(n, i+1 ,n * (i+1)))

# 2741
n = int(input())
for i in range(1, n+1):
    print(i)

# 2742
n = int(input())
for i in range(n):
    print(n-i)