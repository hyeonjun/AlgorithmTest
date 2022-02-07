n = int(input())
mp, mf, ms, mv = map(int, input().split()) # 기준
board = [list(map(int, input().split())) for _ in range(n)] # 단백질, 지방, 탄수화물, 비타민, 가격
ansCost, ansNums = 1e9, []
def dfs(arr, nums, idx):
    global ansCost, ansNums
    if arr[0] >= mp and arr[1] >= mf and arr[2] >= ms and arr[3] >= mv:
        if ansCost > arr[4]:
            ansCost = arr[4]
            ansNums = nums[:]
        elif ansCost == arr[4]:
            ansNums = sorted((ansNums, nums))[0][:]
        return
    if idx == n:
        return
    for i in range(idx, n):
        for j in range(5):
            arr[j] += board[i][j]
        nums.append(i+1)

        dfs(arr, nums, i+1)

        for j in range(5):
            arr[j] -= board[i][j]
        nums.pop()

dfs([0 for _ in range(5)], [], 0)
if ansCost == 1e9:
    print(-1)
else:
    print(ansCost)
    print(*ansNums)