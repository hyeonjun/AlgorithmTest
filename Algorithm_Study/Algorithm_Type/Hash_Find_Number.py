def solution(n, m):
    result = []
    for i in m:
        result.append('1') if i in n else result.append('0')
    return '\n'.join(result)

print(solution([4,1,5,2,3], [1,3,7,9,5]))
