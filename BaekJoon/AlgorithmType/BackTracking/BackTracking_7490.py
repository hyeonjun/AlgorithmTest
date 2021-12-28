def dfs(idx, exp):
    if idx == n:
        if eval(exp.replace(' ', '')) == 0:
            answer.append(exp)
        return
    for op in ['+', '-', ' ']:
        exp += op+str(idx+1)
        dfs(idx+1, exp)
        exp = exp[:-2]

for _ in range(int(input())):
    n = int(input())
    answer = []
    dfs(1, '1')
    for a in sorted(answer):
        print(a)
    print()