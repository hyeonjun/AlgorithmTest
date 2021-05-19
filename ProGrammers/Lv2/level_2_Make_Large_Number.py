def solution(number, k):
    answer = []
    number = list(number)
    for i in number:
        if len(answer) == 0:
            answer.append(i)
        else:
            check = i
            try:
                while answer[-1] < check and k != 0:
                    answer.pop()
                    k -= 1
                answer.append(check)
            except:
                answer.append(check)
    return "".join(answer)[:(len(number)-k)]

print(solution("1924", 2)) # "94"
print(solution("1231234", 3)) # "3234"
print(solution("4177252841", 4)) # "775841"
print(solution("14896532", 7)) # "9"

