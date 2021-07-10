def solution(begin, end):
    answer = []

    for i in range(begin, end + 1):
        if i == 1: # 1일때는 0
            answer.append(0)
        else:
            # 소수 판별
            for j in range(2, int(i ** 0.5) + 1):
                # 전체 길이는 10**9이지만 블록은 10**7이다
                # 그러므로 몫이 10**7을 넘으면 안된다
                if i // j > 10 ** 7:
                    continue
                if i % j == 0: # 소수가 아닐때 나눠지는 것중 가장 먼저 나눠지는 몫을 넣어야함
                    answer.append(i // j)
                    break
            else:
                answer.append(1)
    return answer

print(solution(1, 10)) # [0, 1, 1, 2, 1, 3, 1, 4, 3, 5]