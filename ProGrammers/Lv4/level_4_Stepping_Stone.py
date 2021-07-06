def solution(distance, rocks, n): # 이분탐색
    rocks.sort()
    rocks.append(distance)
    answer = 0
    left, right = 0, distance # 이분탐색의 기준을 거리의 값으로 잡아야함 -> 삭제해야할 바위 결정
    while left <= right:
        prev = 0
        minV = float('inf')  # 바위 사이 최소 거리
        remove = 0
        mid = (left + right) // 2  # 바위 사이 최소 거리(기준)

        for i in range(len(rocks)): # 두 바위의 거리가
            if rocks[i] - prev < mid: # 기준 거리보다 작은 위치의 바위는 삭제
                remove += 1
            else: # 기준 거리보다 크면 이전(prev) 바위 위치 변경
                minV = min(minV, rocks[i] - prev)
                prev = rocks[i]

        if remove > n: # 해당 기준 거리로 풀었을 때 삭제된 바위가 n보다 크다면
            right = mid - 1 # 기준 거리를 더 작은 경우로 탐색해야한다.
        else: # 삭제할 수 있는 바위 개수보다 같거나 작으면
            answer = minV # 바위 최소거리값이 answer이 되고
            left = mid + 1 # 최소거리값 중 큰값을 구하기 위해 기준 거리를 늘림
    return answer

print(solution(25, [2,14,11,21,17], 2)) # 4