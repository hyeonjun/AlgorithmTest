from itertools import combinations
exp = list(input())
stack = []
answer = set()
bracket = [] # 괄호 연결 인덱스 위치 저장
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        bracket.append([stack.pop(), i])

for i in range(1, len(bracket)+1):
    for combi in combinations(bracket, i):
        tmp = exp[:]
        for x, y in combi: # 제거할 괄호 위치
            tmp[x], tmp[y] = '', ''
        answer.add(''.join(tmp))

for a in sorted(answer):
    print(a)