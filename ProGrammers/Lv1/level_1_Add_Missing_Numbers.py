def solution(numbers):
    return sum([i for i in range(10) if i not in numbers])

print(solution([1,2,3,4,6,7,8,0])) # 14
print(solution([5,8,4,0,6,7,9])) # 6