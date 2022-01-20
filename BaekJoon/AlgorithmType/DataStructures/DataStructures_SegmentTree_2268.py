import sys
input = sys.stdin.readline

def update(idx, value):
    node = idx + N
    tree[node] = value
    node //= 2
    while node > 0:
        tree[node] = tree[node*2] + tree[node*2 + 1]
        node //= 2

def query(left, right):
    left, right = left+N, right+N
    result = 0
    while left <= right:
        if left % 2 == 1:
            result += tree[left]
            left += 1
        if right % 2 == 0:
            result += tree[right]
            right -= 1
        left //= 2
        right //= 2
    return result

n, m = map(int, input().split())
N = 1
while N < n:
    N *= 2

tree = [0 for _ in range(N * 2)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0: # sum
        if b > c:
            b, c = c, b
        print(query(b-1, c-1))
    else:
        update(b-1, c)