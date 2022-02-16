n = int(input())

if n < 11:
    print(n-1)
elif n > 1024:
    print(-1)
else:
    answer, idx = -1, 10
    def dfs(nums, depth):
        global answer, idx
        if depth == limit:
            idx += 1
            if idx == n:
                answer = int(nums)
                return
        for i in range(int(nums[-1])):
            dfs(nums+str(i), depth+1)

    for i in range(1, 11): # 자리수, 줄어드는 수의 최대값은 9876543210이므로 최대 10자리까지
        limit = i
        for j in range(1, 10):
            dfs(str(j), 0)

    print(answer)
