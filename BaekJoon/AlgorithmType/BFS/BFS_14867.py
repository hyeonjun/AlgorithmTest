A, B, C, D = map(int, input().split())

def bfs():
    queue = [(0, 0, 0)]
    visited = set()
    visited.add((0, 0))
    while queue:
        x, y, cnt = queue.pop(0)
        if (x, y) == (C, D):
            return cnt
        # x에 가득채우기
        if (A, y) not in visited:
            queue.append((A, y, cnt+1))
            visited.add((A, y))
        # y에 가득 채우기
        if (x, B) not in visited:
            queue.append((x, B, cnt+1))
            visited.add((x, B))
        # x 비우기
        if (0, y) not in visited:
            queue.append((0, y, cnt+1))
            visited.add((0, y))
        # y 비우기
        if (x, 0) not in visited:
            queue.append((x, 0, cnt+1))
            visited.add((x, 0))
        # x -> y로 옮기기
        if x <= B - y: # x에 있는 양이 y의 남아있는 공간보다 적거나 같으면
            if (0, x+y) not in visited:
                queue.append((0, x+y, cnt+1))
                visited.add((0, x+y))
        else:
            if (x+y-B, B) not in visited:
                queue.append((x+y-B, B, cnt+1))
                visited.add((x+y-B, B))
        # y -> x로 옮기기
        if y <= A - x:
            if (x+y, 0) not in visited:
                queue.append((x+y, 0, cnt+1))
                visited.add((x+y, 0))
        else:
            if (A, x+y-A) not in visited:
                queue.append((A, x+y-A, cnt+1))
                visited.add((A, x+y-A))
    return -1

print(bfs())