# set 함수
import sys
s = set()
for _ in range(int(input())):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    x = int(cmd[1])
    if cmd[0] == "add": # x 추가
        s.add(x)
    elif cmd[0] == "remove": # x 제거
        s.discard(x)
    elif cmd[0] == "check": # x 있으면 1, 없으면 0
        print(1 if x in s else 0)
    elif cmd[0] == "toggle": # x가 있으면 삭제, 없으면 추가
        s.add(x) if x not in s else s.discard(x)


# 비트마스크
import sys
bit = 0
for _ in range(int(input())):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) == 1:
        if cmd[0] == "all":
            bit = (1 << 21) - 1 # 1111 1111 1111 1111 1111
        else:
            bit = 0
        continue

    num = int(cmd[1])
    if cmd[0] == "add":
        bit |= (1 << num)
    elif cmd[0] == "remove":
        bit &= ~(1 << num)
    elif cmd[0] == "check":
        print(0 if bit & (1 << num) == 0 else 1)
    elif cmd[0] == "toggle":
        bit ^= (1 << num) # XOR 연산