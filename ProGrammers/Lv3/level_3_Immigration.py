def solution(n, times):
    start = 1
    end = max(times) * n
    while start < end:
        mid = (start + end) // 2
        value = 0

        for i in times:
            value += mid // i

        if value >= n:
            end = mid
        else:
            start = mid + 1
    return start

print(solution(6, [7,10])) # 28