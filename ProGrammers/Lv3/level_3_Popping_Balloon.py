def solution(a):
    answer = 2
    left, right = a[0], a[-1]
    for i in range(1, len(a)-1):
        if left > a[i]:
            # print("left", left, a[i])
            answer += 1
            left = a[i]
        if right > a[-1-i]:
            # print("right", right, a[-1-i])
            answer += 1
            right = a[-1-i]
    return answer if left != right else answer-1

print(solution([9,-1,-5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6