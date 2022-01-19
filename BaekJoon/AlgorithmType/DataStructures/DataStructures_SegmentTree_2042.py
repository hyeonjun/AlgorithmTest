def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start+end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def update(node, start, end, idx, value):
    if idx < start or end < idx:
        return tree[node]
    if start == end == idx:
        tree[node] = value
        return tree[node]
    mid = (start + end) // 2
    tree[node] = update(node*2, start, mid, idx, value) + update(node*2+1, mid+1, end, idx, value)
    return tree[node]

def query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [0 for _ in range(n*4 + 1)]
init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1: # b번째 수를 c로 바꿈
        update(1, 0, n-1, b-1, c)
    else: # b번째 수부터 c번째 수까지의 합
        print(query(1, 0, n-1, b-1, c-1))