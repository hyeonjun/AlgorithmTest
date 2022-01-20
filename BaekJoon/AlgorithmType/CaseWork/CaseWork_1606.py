x, y = map(int, input().split())
answer = 0
while y > 1:
    y -= 1
    x += 1
    answer += 1
if y == 1:
    answer += 1
print(answer + 3 * x * (x+1)+1)