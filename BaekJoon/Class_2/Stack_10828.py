import sys
stack = []
for _ in range(int(sys.stdin.readline())):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        print(stack.pop()) if stack else print("-1")
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print("1") if not stack else print("0")
    elif cmd == "top":
        print(stack[-1]) if stack else print("-1")
    else:
        stack.append(cmd.split()[1])