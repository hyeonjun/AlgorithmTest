# 2467번 문제는 용액이 이미 오름차순으로 정렬되어 들어오지만 2470번 문제는 정렬된 상태가 아니다.
n = int(input())
solution = sorted(list(map(int, input().split())))
left, right = 0, n-1
answer = [abs(solution[left] + solution[right]), (solution[left], solution[right])]
while left < right:
    tmp = solution[left] + solution[right]
    if abs(tmp) < answer[0]:
        answer[0] = abs(tmp)
        answer[1] = (solution[left], solution[right])
    if tmp < 0:
        left += 1
    elif tmp > 0:
        right -= 1
    else:
        print(*answer[1])
        exit(0)
print(*answer[1])