n = int(input())
num, op = [], []
exp = input()
for e in exp:
    if e.isdigit():
        num.append(e)
    else:
        op.append(e)

def dfs(idx, value): # 연산자 인덱스, 계산결과값
    global answer
    if idx == len(op):
        answer = max(answer, int(value))
        return
    # 괄호 추가로 먼저 계산되거나
    dfs(idx+1, str(eval(value+op[idx]+num[idx+1])))
    # 괄호 때문에 나중에 계산되거나
    if idx+1 < len(op): # 연산을 두개 해야하므로 다음 수는 idx+2가 된다.
        # result op1 (num2 op2 num3) => 이전 결과값 이후에 괄호를 넣는다
        # 그래서 먼저 num2 op2 num3을 계산한 후 그 결과와 이전 결과값과 계산한 다음
        # 재귀를 호출해야 한다.
        dfs(idx+2, str(eval(value+op[idx]+str(eval(num[idx+1]+op[idx+1]+num[idx+2])))))

answer = -1e9
dfs(0, num[0])
print(answer)