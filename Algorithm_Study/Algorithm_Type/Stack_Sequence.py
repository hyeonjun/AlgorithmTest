# 스택, 그리디
def solution(N, sequence):
    result = []
    stack = []
    tmp = 1
    for i in range(1, N+1):
        while tmp <= sequence[i-1]:
            stack.append(tmp)
            result.append('+')
            tmp += 1
        if stack[-1] == sequence[i-1]:
            stack.pop()
            result.append('-')
        else:
            return 'NO'
    return "\n".join(result)

print(solution(8, [4,3,6,8,7,5,2,1]))
print(solution(5, [1,2,5,3,4]))
