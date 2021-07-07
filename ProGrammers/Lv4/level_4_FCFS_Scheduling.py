def solution(n, cores): # 효율성 실패
    time = 0
    while n>0:
        for i in range(len(cores)):
            if time % cores[i] == 0:
                n -= 1
                if n ==0:
                    return i+1
        time += 1
print(solution(6, [1,2,3]))

def solution(n, cores): # binary search
    if n <= len(cores):
        return n

    n -= len(cores)
    left = 1
    right = max(cores) * n

    while left < right:
        mid = (left+right) // 2
        w = 0
        for i in cores:
            w += mid // i

        if w >= n:
            right = mid
        else:
            left = mid+1

    for i in cores:
        n -= (right-1) // i
    for i in range(len(cores)):
        if right % cores[i] == 0:
            n -= 1
            if n == 0:
                return i+1
print(solution(6, [1,2,3]))

def solution(n, cores): # parametric search
    if n <= len(cores):
        return n

    # 모든 코어가 동일한 최소, 최대 작업 시간을 가진다고 가능했을 때
    minTime = min(cores) * (n - len(cores)) // len(cores)  # 최소 작업 시간(left)
    maxTime = max(cores) * (n - len(cores)) // len(cores)  # 최대 작업 시간(right)

    while (minTime <= maxTime):
        mid = (minTime + maxTime) // 2
        w = len(cores)  # 작업 수
        current = 0
        for i in cores:
            w += (mid // i)  # mid 시간을 기준으로 코어의 작업량 구함
            if mid % i == 0:
                current += 1  # 지금 작업을 할당받은 코어 개수

        if n > w:  # 수행해야할 작업량이 mid 시간을 기준으로 코어들의 총 작업량보다 크면
            minTime = mid + 1
        elif n <= (w - current):
            maxTime = mid - 1
        else: # 현재까지 처리한 작업 수 < n <= 현재까지 처리한 작업 수 + 처리되고 있는 작업수
            tmp = w - current
            for i in range(len(cores)):
                if mid % cores[i] == 0:
                    tmp += 1
                if tmp == n:
                    return i + 1
print(solution(6, [1,2,3]))