import sys
input = sys.stdin.readline
n = int(input())
solution = sorted(list(map(int, input().split())))
answer = [sys.maxsize, []]

for idx in range(n-2): # left, right를 빼고 n-3까지 움직일 수 있음
    left = idx+1
    right = n-1
    while left < right:
        tmp = solution[idx] + solution[left] + solution[right]
        if abs(tmp) < answer[0]:
            answer[0] = abs(tmp)
            answer[1] = [solution[idx], solution[left], solution[right]]
        if tmp < 0:
            left += 1
        elif tmp > 0:
            right -= 1
        else:
            print(*answer[1])
            exit(0)
print(*answer[1])