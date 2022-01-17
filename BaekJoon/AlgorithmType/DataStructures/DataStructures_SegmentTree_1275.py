"""
세그먼트 트리 - 구간 트리
배열 A
- 1. 구간 l ~ r : A[l] + ... A[r]
- 2. i번째 수를 v로 변경: A[i] = v
    => O(NM) + O(M) = O(NM)

** 세그먼트 트리 이용 - 1번 연산 O(logN), 2번 연산 O(logN) 만에 수행 가능
    - 리프 노드 : 배을의 그 수 자체
    - 리프 노드가 아닌 다른 노드 : 왼쪽 자식과 오른쪽 자식의 합
        - 어떤 노드 번호가 x, 왼쪽 자식 번호는 2*x, 오른쪽 자식 번호는 2*x+1
"""
# init : 세그먼트 트리 생성(루트부터 아래로 반씩 나눠서)
def init(node, start, end):
    if start == end: # 리프 노드 : 해당 범위에 노드 하나 - 그 수 자체
        tree[node] = arr[start]
        return tree[node]
    # 범위에 노드가 두 개 이상이면
    mid = (start + end) // 2
    tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end) # 왼쪽 자식 노드, 오른쪽 자식 노드
    return tree[node]

# update : 값 업데이트
def update1(node, start, end, idx, value): # 6916 ms
    if idx < start or idx > end: # 값 변경되는 리프와 상관 없는 노드들
        return
    tree[node] += value
    if start != end:
        mid = (start+end) // 2
        update1(node*2, start, mid, idx, value)
        update2(node*2+1, mid+1, end, idx, value)

def update2(node, start, end, idx, value): # 7272 ms
    if idx < start or idx > end:
        return tree[node]

    if start == end == idx:
        tree[node] = value
        return tree[node]

    mid = (start + end) // 2
    tree[node] = update2(node * 2, start, mid, idx, value) + update2(node * 2 + 1, mid + 1, end, idx, value)
    return tree[node]

# query : 구간 합
def query(node, start, end, left, right):
    if right < start or end < left: # 범위 바깥에 있는 노드들은 무시
        return 0
    if left <= start and end <= right: # 노드가 범위 안에 포함되면
        return tree[node]
    mid = (start+end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)



n, q = map(int, input().split())
arr = list(map(int, input().split()))

# segment tree
tree = [0 for _ in range(n*4 + 1)]
init(1, 0, n-1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    x, y = min(x, y), max(x, y) # start, end
    print(query(1, 0, n-1, x-1, y-1))

    # 값 변경 - update 1
    # value = b - arr[a-1] # a번째 노드의 값을 b로 바꾸기 위해 변경될만큼의 값을 구한다.
    # arr[a-1] = b # a번째 노드 값을 b로 바꾸고
    # update1(1, 0, n-1, a-1, value) # value를 더하게 함으로써 변경하게 된다.

    update2(1, 0, n-1, a-1, b)
