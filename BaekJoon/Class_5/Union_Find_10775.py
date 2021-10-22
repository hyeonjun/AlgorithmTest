import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
arr = [int(input()) for _ in range(p)]
parent = list(range(g+1))

# 시간초과
# def find(n):
#     if parent[n] == n:
#         return n
#     return find(parent[n])

# 통과
def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a, b= find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for i in arr:
    x = find(i)
    if x == 0:
        break
    union(x, x-1)
    answer += 1
print(answer)