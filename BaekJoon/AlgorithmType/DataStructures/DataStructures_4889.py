cnt = 1
while True:
    bracket = input()
    if '-' in bracket:
        break
    stack = []
    answer = 0
    for b in bracket:
        if not stack and b == '}':
            answer += 1
            stack.append('{')
        elif stack and b == '}':
            stack.pop()
        elif b == '{':
            stack.append(b)
    answer += len(stack) // 2 # 절반은 '}'로 바꿔야함
    print(f'{cnt}. {answer}')
    cnt += 1