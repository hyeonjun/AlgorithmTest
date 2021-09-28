import sys
queue = []
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        print(queue.pop(0)) if queue else print("-1")
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print("1") if not queue else print("0")
    elif cmd == "front":
        print(queue[0]) if queue else print("-1")
    elif cmd == "back":
        print(queue[-1]) if queue else print("-1")
    else:
        queue.append(cmd.split()[1])