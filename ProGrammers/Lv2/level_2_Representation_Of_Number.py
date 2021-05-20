def solution(num):
    answer = [i  for i in range(1,num+1,2) if num % i == 0]
    print(answer)
    return len(answer)


def solution(n):
    answer = 0
    for i in range(1, n//2 + 1):
        tmp = 0
        for j in range(i, n//2 + 2):
            tmp += j
            if tmp == n:
                answer += 1
            elif tmp > n:
                break
    return answer+1


print(solution(15))