n, p = map(int, input().split())
stack = [[] for _ in range(7)] # 1~6번 줄 스택
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    if not stack[x]:
        stack[x].append(y)
        answer += 1
    else: # 줄에 음계를 누르고 있을 때
        if stack[x][-1] < y: # 새로 누를 곳이 이전에 누른 곳보다 크면
            stack[x].append(y)
            answer += 1
        elif stack[x][-1] > y: # 보다 작으면
            while stack[x]:
                if stack[x][-1] <= y:
                    break
                stack[x].pop()
                answer += 1
            if stack[x] and stack[x][-1] == y:
                continue
            stack[x].append(y)
            answer += 1
        else:
            continue
print(answer)