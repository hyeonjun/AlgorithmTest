def solution(numbers):
    answer = []
    for i in numbers:
        tmp = list('0' + bin(i)[2:])
        idx = ''.join(tmp).rfind('0')
        tmp[idx] = '1'
        if i % 2 == 1:
            tmp[idx+1] = '0'
        answer.append(int(''.join(tmp), 2))
    return answer

print(solution([2, 7]))

def solution(numbers): # 시간초과? 왜지,,?
    answer = []
    for i in range(len(numbers)):
        tmp = numbers[i] + 1
        while True:
            n = str(bin(numbers[i] & tmp)[2:])
            n = n.rjust(len(bin(tmp)[2:]), '0')
            if n.count('0') <= 2:
                answer.append(tmp)
                break
            tmp += 1
    return answer

print(solution([2, 7]))