"""
기본적으로 parent[i]에 부모 노드를 저장하는 것은 동일.
i가 루트 노드일 경우 집합의 size를 음수로 저장하게 된다.
즉, parent[i]가 음수일 경우 그 수의 절대값은 size이고, 양수일 경우 그 값은 부모 노드를 가리킨다.

ex)
parent[2] = -3일 경우 2번 노드 밑에 두개의 노드가 더 있어서 총 3개의 노드가 집합을 이루고 있다는 뜻.
parent[3 = 5일 경우 3번 노드의 부모 5번 노드라는 뜻이다.
"""
n, m = map(int, input().split())
parent = [-1 for _ in range(n+1)]

def find(n):
    if parent[n] < 0:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if parent[a] < parent[b]:
        parent[a] += parent[b]
        parent[b] = a
    else:
        parent[b] += parent[a]
        parent[a] = b

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")


# 일반 Union_Find, 더 빠르긴하다
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int,input().split())

parent = [0] * (N+1) # 부모 테이블 생성
for i in range(N+1): # 자기 자신을 부모로 설정
    parent[i] = i

# 루트 노드 찾는 함수
def find(a):
    if a == parent[a]: # 자기 자신이 루트 노드이면 a 반환
        return a
    p = find(parent[a]) # a의 루트 노드 찾기
    parent[a] = p # 부모 테이블 갱신
    return parent[a] # a의 루트 노드 반환

# a가 속해있는 집합과 b가 속해있는 집합을 합치는 연산
def union(a,b):
    a = find(a) # a의 루트 노드 찾기
    b = find(b) # b의 루트 노드 찾기

    if a == b: # a와 b의 루트 노드가 같으면 동일한 집합
        return
    if a < b: # a와 b의 루트 노드가 다르면 두 집합을 합치기
        parent[b] = a
    else:
        parent[a] = b

for _ in range(M):
    o, a, b = map(int,input().split()) # operation, 원소, 원소
    if o == 0: # o=0은 두 원소가 포함되어 있는 집합을 합치기
        union(a,b)
    elif o == 1: # 두 원소가 동일한 집합인지 판단
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')