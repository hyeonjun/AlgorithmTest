from collections import deque
from itertools import combinations
n, k = input().split()
candi = list(combinations(list(range(len(n))), 2))

def bfs(start):
    queue = deque([(list(start), 0, int(start))])
    answer = -1
    while queue:
        visited = set()
        tmp = deque()
        for _ in range(len(queue)):
            x, cnt, num = queue.popleft()
            if cnt == int(k):
                if answer < num:
                    answer = num
                continue
            for i, j in candi:
                nx = x[:]
                nx[i], nx[j] = nx[j], nx[i]
                if nx[0] == '0': continue
                nnum = int(''.join(nx))
                if nnum not in visited:
                    visited.add(nnum)
                    tmp.append((nx, cnt+1, nnum))
        queue = tmp
    return answer

print(bfs(n))