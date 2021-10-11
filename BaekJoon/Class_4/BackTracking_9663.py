n = int(input())
queen = [0 for _ in range(n)]
visited = [False for _ in range(n)]
answer = 0
"""
  0 1 2 3
0 - * - * -> 같은 열
1 - * - - -> 같은 행
2 * - - - => 대각선
3 - * - -
"""
def check(row):
    for i in range(row):
        #         같은 열 확인                대각선 확인
        if queen[i] == queen[row] or abs(queen[row]-queen[i]) == row-i:
            return False
    return True

def dfs(row):
    global answer
    if row == n: # 마지막 줄까지 확인했으면 가능
        answer += 1
    else:
        for i in range(n):
            if visited[i]:
                continue
            queen[row] = i
            if check(row):
                visited[i] = True
                dfs(row+1)
                visited[i] = False
    return answer

print(dfs(0))