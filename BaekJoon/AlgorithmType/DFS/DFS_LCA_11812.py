# 최소 공통 조상(LCA)
# 문제: K진 트리에서 두 노드 X와 Y 사이의 거리 구하기
# 이진 트리에서 자식은 Node * 2, 부모는 Node / 2 이다
# 예)
# 3진 트리
"""
         1
  2      3      4
5 6 7
"""
# 즉, 자식은 Node * k + 1
# 부모는 (Node + (k-2)) / k
#    => Node * k + 1까지가 자식이기 때문에

input = __import__("sys").stdin.readline
n, k, q = map(int, input().split()) # 노드 개수, k진, 거리를 구해야하는 노드 쌍 개수

def getParent(node, k):
    return (node + k - 2) // k

for _ in range(q):
    x, y = map(int, input().split())
    if x > y: x, y = y, x
    if k == 1:
        print(y - x)
        continue
    distance = 0
    while x != y:
        while x < y:
            distance += 1
            y = getParent(y, k)
            if x > y: x, y = y, x
    print(distance)