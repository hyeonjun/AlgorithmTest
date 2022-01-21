# 세그먼트 트리를 사용하여 구간별 최대값, 최소값 구하기
def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]
    mid = (start + end) // 2
    init(node*2, start, mid)
    init(node*2+1, mid+1, end)
    tree[node] = (
        min(tree[node*2][0], tree[node*2+1][0]),
        max(tree[node*2][1], tree[node*2+1][1])
    )
    return tree[node]

def MinMaxQuery(node, start, end, left, right):
    if left <= start and end <= right:
        return tree[node]

    minN, maxN = [], []
    mid = (start + end) // 2
    if left <= mid and start <= right:
        minV, maxV = MinMaxQuery(node*2, start, mid, left, right)
        minN.append(minV)
        maxN.append(maxV)
    if left <= end and mid+1 <= right:
        minV, maxV = MinMaxQuery(node*2+1, mid+1, end, left, right)
        minN.append(minV)
        maxN.append(maxV)
    return min(minN), max(maxN)

import sys
input=sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree = [(-1, -1) for _ in range(4*n)]
init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*MinMaxQuery(1, 0, n-1, a-1, b-1))