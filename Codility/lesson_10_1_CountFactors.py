def solution(N):
    import math
    count = 0
    for i in range(1, int(math.sqrt(N))+1):
        if i*i == N:
            count += 1
            break
        if N % i == 0:
            count+= 2
    return count
    pass


print(solution(169))
print(solution(24))
print(solution(211213542352))