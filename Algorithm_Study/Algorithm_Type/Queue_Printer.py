def solution(n,m,printer):
    count = 0
    queue = [(idx, v) for idx, v in enumerate(printer)]
    while True:
        if queue[0][1] == max(queue, key=lambda x:x[1])[1]:
            count += 1
            data = queue.pop(0)
            if data[0] == m:
                return count
        else:
            queue.append(queue.pop(0))

print(solution(1,0,[5])) # 1
print(solution(4,2,[1,2,3,4])) # 2
print(solution(6,0,[1,1,9,1,1,1])) # 5