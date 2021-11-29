"""
0, 양수 = 덧셈
0, 음수 = 곱셈

1, 수 = 덧셈

양수, 양수 = 곱셈
양수, 음수 = 덧셈
음수, 음수 = 곱셈
"""
n = int(input())
positive, negative = [], []
answer = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        positive.append(num)
    elif num == 1:
        answer += 1
    else:
        negative.append(num)
positive.sort(reverse=True)
negative.sort()
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        answer += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        answer += positive[i] * positive[i+1]
    answer += positive[-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        answer += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        answer += negative[i] * negative[i+1]
    answer += negative[-1]

print(answer)