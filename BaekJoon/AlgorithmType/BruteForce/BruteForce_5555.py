target = input()
n = int(input())
answer = 0
for _ in range(n):
    data = input()
    if target in data+data:
        answer += 1
print(answer)