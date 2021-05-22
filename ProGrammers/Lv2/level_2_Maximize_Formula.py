def solution(expression):
    answer = []
    from itertools import permutations
    import re
    oper = [i for i in ['*', '-', '+'] if i in expression]
    oper = [j for j in permutations(oper)]
    expression = re.split(r'(\D)', expression)
    for op in oper:
        exp = expression.copy()
        for o in op:
            while o in exp:
                tmp = exp.index(o)
                exp[tmp-1] = str(eval("".join(exp[tmp-1:tmp+2])))
                exp = exp[:tmp]+exp[tmp+2:]
        answer.append(abs(int(exp[-1])))
    return max(answer)

print(solution("100-200*300-500+20")) # 60420
print(solution("50*6-3*2")) # 300