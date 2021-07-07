# Mixing Milk
def solution(bucket):
    n = len(bucket)
    for i in range(100):
        if bucket[i % n][1] + bucket[(i+1) % n][1] <= bucket[(i+1) % n][0]:
            bucket[(i + 1) % n][1] += bucket[i % n][1]
            bucket[i % n][1] = 0
        else:
            bucket[i % n][1] -= bucket[(i+1) % n][0]
            bucket[(i+1) % n][1] += bucket[(i+1) % n][0]
        # print(i, bucket)
    answer = []
    for c, m in bucket:
        answer.append(m)
    return answer

print(solution([[10,3],[11,4],[12,5]])) # [0, 10, 2]

def solution(bucket):
    for i in range(100):
        bucket[i % 3][1], bucket[(i+1) % 3][1] = \
            max(bucket[i % 3][1] - (bucket[(i+1)% 3][0] - bucket[(i+1) % 3][1]),
                0), min(bucket[(i+1) % 3][0], bucket[(i+1) % 3][1] + bucket[i % 3][1])

    return [m for c, m in bucket]

print(solution([[10, 3], [11, 4], [12, 5]])) # [0, 10, 2]
