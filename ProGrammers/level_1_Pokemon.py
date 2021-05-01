def solution(nums):
    N = len(nums)//2
    return len(set(nums)) if len(set(nums)) <= N else N

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))