def solution(s):
    s = s.split(' ')
    answer = []
    for w in s:
        words = ""
        for i, v in enumerate(w):
            words += v.upper() if i % 2 == 0 else v.lower()
        answer.append(words)

    return " ".join(answer)

print(solution("try hello world"))