def solution(s):
    answer = []

    def extract(s):
        count, stack = 0, []
        for i in s:
            if i == '0' and stack[-2:] == ['1', '1']:
                stack.pop()
                stack.pop()
                count += 1  # 110 개수
            else:
                stack.append(i)
        return ''.join(stack), count

    def inserts(s):
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                return s[:i+1] + '110' + s[i+1:]
        return '110' + s

    for i in s:
        i, count = extract(i)
        for _ in range(count):
            i = inserts(i)
        answer.append(i)
    return answer

print(solution(["1110","100111100","0111111010"]))
print(solution(["1011110","01110","101101111010"]))