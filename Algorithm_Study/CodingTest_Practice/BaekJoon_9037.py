# The candy war
def solution(n, candy):
    # def check(n, array):
    #     for a in range(n):
    #         if array[a] != array[(a+1) % n]:
    #             return False
    #     return True

    def check(n, array):
        for i in range(n):
            if candy[i] % 2 != 0:
                candy[i] += 1
        return len(set(candy)) == 1

    for i in range(n): # 짝수 맞추기 -> 순환 횟수 포함 x
        if candy[i] % 2 != 0:
            candy[i] += 1

    answer = 0

    while not check(n, candy):
        tmp = [candy[i] // 2 for i in range(n)]
        for i in range(n):
            candy[i] -= tmp[i]
            candy[(i+1)%n] += tmp[i]

        # for i in range(n):
        #     if candy[i] % 2 != 0:
        #         candy[i] += 1
        answer += 1
    return answer


print(solution(5,[2,4,7,8,9])) # 6
print(solution(1,[9])) # 0
print(solution(6,[10,5,13,2,7,8])) # 4
print(solution(4,[3,4,4,3])) # 0
