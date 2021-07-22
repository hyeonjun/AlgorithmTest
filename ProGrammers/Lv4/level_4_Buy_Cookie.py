def solution(cookie):
    answer = 0
    for i in range(len(cookie) - 1):  # 기준점
        left, right = i, i + 1
        lsum, rsum = cookie[i], cookie[i + 1]

        while True:
            if lsum == rsum:
                answer = max(answer, lsum)

            if left > 0 and lsum <= rsum:
                left -= 1
                lsum += cookie[left]
            elif right < len(cookie) - 1 and rsum <= lsum:
                right += 1
                rsum += cookie[right]
            else:
                break
    return answer

print(solution([1,1,2,3])) # 3
print(solution([1,2,4,5])) # 0