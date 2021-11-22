n, m = map(int, input().split())
J = int(input())
apple = [int(input()) for _ in range(J)]
start, end = 1, m
answer = 0
for i in apple:
    if start > i:
        answer += start-i
        start, end = i, end-(start-i)
    elif end < i:
        answer += i-end
        start, end = start+(i-end), i
print(answer)