from itertools import combinations
arr = list(map(int, input().split()))
answer = min(arr)
while True:
    flag = False
    for x, y, z in combinations(arr, 3):
        if answer % x == 0 and answer % y == 0 and answer % z == 0:
            flag = True
            break
    if flag:
        print(answer)
        break
    answer += 1