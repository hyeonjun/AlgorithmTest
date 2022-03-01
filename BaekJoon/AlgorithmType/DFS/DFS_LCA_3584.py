"""
LCA(Lowest Common Ancestor) - 최소 공통 조상
: 두 정점 u, v에서 가장 가까운 공통 조상을 찾는 과정

각 노드의 부모 노드들을 모두 저장한 뒤 루트 노드부터 차례대로 내려오며
비교해 같지 않은 노드가 나올 때까지 반복.
    처음 같지 않는 노드가 나왔을 때 그 노드의 부모가 최소공통조상이다.
"""
for _ in range(int(input())):
    n = int(input())
    parent = [0 for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a

    a, b = map(int, input().split())
    A, B = [a], [b]

    # 각 노드의 부모 노드가 루트가 나올 때까지 모든 부모 노드 저장 => 최상위 루트인 경우 parent 리스트 값이 0
    while parent[a]:
        A.append(parent[a])
        a = parent[a]
    while parent[b]:
        B.append(parent[b])
        b = parent[b]

    # 같은 레벨로 맞추고 부모 노드 같은 것 찾기
    aLevel, bLevel = len(A)-1, len(B)-1
    # 루트 노드부터 비교
    while A[aLevel] == B[bLevel]:
        aLevel -= 1
        bLevel -= 1
    print(A[aLevel+1])