n = int(input())
solution = list(map(int, input().split()))
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
        print(answer[1][0], answer[1][1])
        exit(0)
print(answer[1][0], answer[1][1])