a, b = input().split()
answer = 0
for n in a:
    for m in b:
        answer += int(n) * int(m)
print(answer)