r, g, b = map(int, input().split())
answer = r // 3 + g // 3 + b // 3 # rrr bbb ggg
r, g, b = r % 3, g %3, b % 3
if [r, g, b].count(0) == 2: # r / g / b
    answer += 1
else:
    answer += max([r, g, b]) # max 값은 무조건 3보다 작은 값.
print(answer)