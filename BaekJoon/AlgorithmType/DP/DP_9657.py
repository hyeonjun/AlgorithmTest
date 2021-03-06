"""
완벽하게 게임을 했다는 말은 어떤 상황에서는 자신이 이기기 위한 돌의 개수를 가져간다는 것.
SK, CY
1 -> SK
2 -> CY
3 -> SK
4 -> SK
5 -> 3, 1 (1) -> 1(0) SK => 4개가 아닌 3개를 가져간다
6 -> 4, 1 (1), 1(0) -> SK
7 -> 4, 3 (0) -> CY / 3, 4(0) -> CY / 1, 4(2), 1, 1(0) -> CY
8 -> 4, 4 CY / 3, 3, 1, 1 CY / 1, 1(6), 4,1, 1 SK

ex) dp[5]에서 3가지(1개, 3개, 4개의 돌 가져가기) 경우의 수를 확인
 -> dp[1], dp[2], dp,[4] => 이중 CY가 이긴 것이 있다면 SK가 이길 경우의 수가 존재한다는 것
 -> 이전에 CY가 이긴 경우의 수가 있다면, CY가 해당 경우의 수로 돌을 가져간 후
    SK가 마지막으로 한번 더 가져갈 수 있는 기회가 생기기 때문

=>
 dp[i] = "SK" if "CY" in [dp[i-1], dp[i-3], dp[i-4]] else "CY"
"""
n = int(input())
dp = ["", "SK", "CY", "SK", "SK"]
for i in range(5, n+1):
    win = "SK" if "CY" in [dp[i-1], dp[i-3], dp[i-4]] else "CY"
    dp.append(win)
print(dp[n])