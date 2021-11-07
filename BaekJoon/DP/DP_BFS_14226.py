"""
화면에 이모티콘 s개를 만들기 위해 필요한 최소 시간
목적지까지 최단시간 -> BFS
목적지에 도달한 최단시간을 기록할 DP
처음에 이모티콘 1개

연산
1. 화면에 있는 이모티콘 개수 -> 클립보드
2. 클립보드에 있는 이모티콘 모두 화면에 붙여넣음
3. 화면에 있는 이모티콘 중 하나 삭제
각 연산은 1초가 걸림
"""
n = int(input())
queue = [(1,0)] # [화면 이모티콘 개수, 클립보드 이모티콘 개수]
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)] # dp[화면 이모티콘 개수][클립보드 이모티콘 개수] = 최단시간
dp[1][0] = 0

while queue:
    s, c = queue.pop(0)
    if s == n:
        print(dp[s][c])
        break
    # 1. 화면 이모티콘 개수 => 클립보드 개수
    if dp[s][s] == -1:
        dp[s][s] = dp[s][c]+1
        queue.append((s, s))
    # 2. 클립보드가 있는 이모티콘을 모두 화면에 붙여넣기
    if s+c < n+1 and dp[s+c][c] == -1:
        dp[s+c][c] = dp[s][c]+1
        queue.append((s+c, c))
    # 3. 화면에 있는 이모티콘 중 하나 삭제
    if s-1 >= 0 and dp[s-1][c] == -1:
        dp[s-1][c] = dp[s][c]+1
        queue.append((s-1, c))