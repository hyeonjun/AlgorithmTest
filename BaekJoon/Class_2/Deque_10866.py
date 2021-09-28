import sys
from collections import deque
deq = deque()
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push_front":
        deq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front":
        print(deq.popleft() if deq else "-1")
    elif cmd[0] == "pop_back":
        print(deq.pop() if deq else "-1")
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        print("1" if not deq else "0")
    elif cmd[0] == "front":
        print(deq[0] if deq else "-1")
    else:
        print(deq[-1] if deq else "-1")
