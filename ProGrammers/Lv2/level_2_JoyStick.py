def solution(name):
    answer = 0
    alpha = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    print(alpha)
    idx = 0
    while True:
        answer += alpha[idx]
        alpha[idx] = 0
        if sum(alpha) == 0:
            break
        right, left = 1, 1

        while alpha[idx + right] == 0:
            right += 1
        while alpha[idx - left] == 0:
            left += 1

        answer += right if right <= left else left
        idx += right if right <= left else -left

    return answer

print(solution("JEROEN")) # 56
print(solution("JAN")) # 23
print(solution("JAZ")) # 11