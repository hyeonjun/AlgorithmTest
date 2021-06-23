def solution(n, stations, w):
    answer = 0
    locate = 1
    idx = 0
    while locate <= n:
        if idx < len(stations) and locate >= stations[idx] - w:
            locate = stations[idx] + w + 1
            idx += 1
        else:
            locate += 2 * w + 1
            answer += 1

    return answer

print(solution(11, [4,11], 1)) # 3
print(solution(16, [9], 2)) # 3