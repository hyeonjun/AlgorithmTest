def solution(arr):
    import re
    answer = "".join([str(i) for i in arr])
    answer = re.sub(r'(.)\1+', r'\1', answer)
    return [int(answer[i]) for i in range(len(answer))]

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))