n = int(input())

enter = {}
for i in range(n):
    car = input()
    enter[car] = i

out = []
for _ in range(n):
    car = input()
    out.append(car)

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if enter[out[j]] < enter[out[i]]:
            answer += 1
            break
print(answer)