n = int(input())
arr = list(map(int, input().split()))
visited = [False for _ in range(100001)]
answer = 0
end = 0
for start in range(n):
    while end < n:
        if visited[arr[end]]: # 이미 방문한 값이라면, 해당 연속 수에 end 값이 이미 들어가 있다는 것
            break
        visited[arr[end]] = True # 방문 확인
        end += 1
    answer += end - start
    visited[arr[start]] = False # start 값에 대한 체크가 끝났으면 방문 해제
print(answer)
