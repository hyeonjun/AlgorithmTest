from collections import deque
n, m = map(int, input().split())
num = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)])

answer = 0
for i in num:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        position = queue.index(i)
        if position < len(queue) - position: # 앞쪽이 가깝다
            while queue[0] != i:
                queue.append(queue.popleft())
                answer += 1
        else:
            while queue[0] != i:
                queue.appendleft(queue.pop())
                answer += 1
print(answer)