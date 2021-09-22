# 10869
a, b = map(int, input().split())
print('{}\n{}\n{}\n{}\n{}'.format(a+b, a-b, a*b, a//b, a%b))

# 10871
n, x = map(int, input().split())
for i in map(int, input().split()):
    if i < x:
        print(i, end=' ')

# 10950
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a+b)

# 10951
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 10952
while True:
    a, b = map(int, input().split())
    if a != 0 and b != 0:
        print(a+b)
    else:
        break

# 10998
a, b = map(int, input().split())
print(a*b)