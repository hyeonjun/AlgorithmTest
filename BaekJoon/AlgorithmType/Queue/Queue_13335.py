n, w, l = map(int, input().split())
truck = list(map(int, input().split()))
answer, sumV = 0, 0
queue = [0 for _ in range(w)]
while truck:
    answer += 1
    sumV -= queue.pop(0)
    if sumV + truck[0] <= l:
        sumV += truck[0]
        queue.append(truck.pop(0))
    else:
        queue.append(0)
print(answer + w)