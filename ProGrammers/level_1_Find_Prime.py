def solution(n):
    import math
    answer = 0
    def prime(N):
        for i in range(2, int(math.sqrt(N))+1):
            if N % i == 0:
                return False
        return True

    for i in range(2, n+1):
        if prime(i):
            answer+=1
    return answer

print(solution(13))

def solution(n):
    num = set(range(2, n+1)) # {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

    for i in range(2, int(n**0.5)+1):
        if i in num:
            num-=set(range(i*i,n+1,i))
    return len(num)

print(solution(13))

