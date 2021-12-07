import sys
from collections import deque
input = sys.stdin.readline
queue = deque([])
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(queue.popleft()) if queue else print("-1")
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print("1") if not queue else print("0")
    elif cmd[0] == "front":
        print(queue[0]) if queue else print("-1")
    elif cmd[0] == "back":
        print(queue[-1]) if queue else print("-1")