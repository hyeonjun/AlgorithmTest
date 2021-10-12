# Union-Find
n, m = map(int, input().split()) # 사람 수, 파티 수
true_lst = list(map(int, input().split()))

parent = [i for i in range(n+1)]
def find(x): # 부모 선정
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return p

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        parent[y] = parent[x]
    pass

for i in range(true_lst[0]):
    union(true_lst[1], true_lst[i + 1]) # 첫 번째 사람을 부모로 선정

party = []
for _ in range(m):
    party.append(list(map(int, input().split())))
    for current in range(party[-1][0]-1):
        union(party[-1][current+1], party[-1][current+2])

answer = 0
for i in party:
    for current in range(i[0]):
        # 파티원들이 진실을 아는 사람의 부모와 동일 -> 해당 파티는 과장 x
        if (len(true_lst) > 1 and find(i[current+1]) == find(true_lst[1])):
            answer += 1
            break
print(m - answer)

# Set 활용
n, m = map(int, input().split())
true_list = set(map(int, input().split()[1:]))
party = []
for _ in range(m):
    party.append(set(map(int, input().split()[1:])))

answer = [1 for _ in range(m)]
for _ in range(m): # true_list가 중간중간에 변경되므로 파티 수만큼 돌려 완탐
    for i,v  in enumerate(party):
        if true_list & v: # 공통 원소가 있으면
            answer[i] = 0
            true_list |= v # 진실을 아는 사람과 마추친 사람은 거짓말을 할 수 없음

print(sum(answer))