from collections import deque
n = deque()
for i in range(int(input())):
    n.append(i+1)

while len(n) > 1:
    n.popleft()
    n.append(n.popleft())
print(n[0])

# 일반 리스트로 pop(0)해도 시간 초과발생, deque()를 사용하면 통과 가능