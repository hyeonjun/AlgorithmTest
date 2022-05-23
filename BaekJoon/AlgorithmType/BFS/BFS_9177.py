from collections import deque
n = int(input())

def bfs():
    a, b, c = words
    queue = deque([(len(a), len(b), len(c))]) # 각 단어 길이 -> 인덱스값만 넣어서 뒤에서부터 비교
    visited = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    while queue:
        al, bl, cl = queue.popleft()
        if al == bl == cl == 0: # 세 단어가 모두 0인덱스가 되었으면 가능 -> True
            return True
        elif cl == 0: return False # 3번째 단어만 끝났으면 False

        if al > 0 and a[al-1] == c[cl-1] and not visited[al-1][bl]:
            queue.append((al-1, bl, cl-1))
            visited[al-1][bl] = True
        if bl > 0 and b[bl-1] == c[cl-1] and not visited[al][bl-1]:
            queue.append((al, bl-1, cl-1))
            visited[al][bl-1] = True
    return False

for i in range(1, n+1):
    words = list(input().split())
    if bfs():
        print(f'Data set {i}: yes')
    else:
        print(f'Data set {i}: no')