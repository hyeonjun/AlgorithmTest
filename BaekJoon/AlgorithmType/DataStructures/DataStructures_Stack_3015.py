"""
* 값이 중복이 있는 문제.
3 3 3 4 일때 4가 3개의 3과 모두 볼 수 있다.
=> 중복이 있는 경우 cnt를 늘려서 저장한다.
서로 볼 수 있는 값이 올때 cnt를 answer에 더한다.
"""
n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
answer = 0
for a in arr:
    while stack and stack[-1][0] < a:
        answer += stack.pop()[1] # cnt 추가

    if not stack:
        stack.append((a, 1))
    else:
        if stack[-1][0] == a: # 중복 값 cnt+1
            cnt = stack.pop()[1]
            answer += cnt
            if stack: # stack에 있는 사람과 새롭게 들어온 중복값도 서로 볼 수 있다
                answer += 1
            stack.append((a, cnt+1))
        else:
            stack.append((a, 1)) # 스택에 값이 있고 새로운 값과 서로 볼 수 있으니 +1
            answer += 1
print(answer)