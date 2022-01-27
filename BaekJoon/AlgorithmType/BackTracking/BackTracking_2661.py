n = int(input())
answer = []
def check(strs):
    strs = strs[::-1]
    for i in range(1, len(strs)//2+1):
        # 추가된 수에 대해 비교 길이를 늘리면서 좋은 수열인지 확인
        if strs[:i] == strs[i:i*2]:
            return False
    return True

endpoint = False

def dfs(depth):
    global answer, endpoint
    if depth == n:
        print(''.join(answer))
        endpoint = True
        return
    for i in ['1', '2', '3']:
        if not check(''.join(answer+[i])):
            continue
        answer.append(i)
        dfs(depth+1)
        if endpoint:
            break
        answer.pop()
dfs(0)