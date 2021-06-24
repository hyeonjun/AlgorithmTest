def solution(stones, k): # 효율성 실패
    answer = 0
    while True:
        for i in range(len(stones)):
            if stones[i] == 0:
                if sum(stones[i:i+k]) == 0 and i <= len(stones)-k:
                    return answer
            else:
                stones[i] -= 1
        answer += 1
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

def solution(stones, k): # 이분 탐색으로 시간복잡도 통과
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for s in stones:
            if s <= mid:
                cnt += 1
                if cnt == k: # 건널수 없다고 판단 -> 최대값을 내림
                    break
            else:
                cnt = 0
        if cnt >= k:
            right = mid - 1
        else: # mid명수만큼은 징검다리를 통과할 수 있다는 것이니, 최소값을 올려 mid값을 증가
            left = mid + 1
    return left

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))