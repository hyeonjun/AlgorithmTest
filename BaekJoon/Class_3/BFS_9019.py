def bfs(a, b):
    queue = [[a, ""]]
    visited = [False for _ in range(10001)]
    while queue:
        num, cmd = queue.pop(0)

        # D 명령
        dn = (num * 2) % 10000
        if dn == b:
            return cmd + "D"
        elif visited[dn] == False:
            visited[dn] = True
            queue.append([dn, cmd + "D"])

        # S 명령
        sn = 9999 if num == 0 else num - 1
        if sn == b:
            return cmd + "S"
        elif visited[sn] == False:
            visited[sn] = True
            queue.append([sn, cmd + "S"])

        # L 명령
        ln = ((num % 1000) * 10) + (num // 1000)
        if ln == b:
            return cmd + "L"
        elif visited[ln] == False:
            visited[ln] = True
            queue.append([ln, cmd + "L"])

        # R 명령
        rn = (num // 10) + ((num % 10) * 1000)
        if rn == b:
            return cmd + "R"
        elif visited[rn] == False:
            visited[rn] = True
            queue.append([rn, cmd + "R"])

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs(a, b))