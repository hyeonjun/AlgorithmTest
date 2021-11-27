"""
주사위
  3
4 0 1 5
  2      일때, 0-5, 1-4, 2-3 으로 대칭

1면이 보이는 개수 : (n-2) * (n-2) + 4 * (n-1) * (n-2)
2면이 보이는 개수 : 4 * (n-2) + 4 * (n-1)
3면이 보이는 개수 : 정육면체의 각 꼭지점으로 4개
"""
n = int(input())
dice = list(map(int, input().split()))
answer = 0
if n == 1:
    dice.sort()
    for i in range(5):
        answer += dice[i]
else:
    dice_list = []
    for i in range(3):
        dice_list.append(min(dice[i], dice[5-i]))
    dice_list.sort()

    # 1면, 2면, 3면의 주사위 최소값
    for i in range(1, 3):
        dice_list[i] += dice_list[i-1]

    # 1면, 2면, 3면이 보이는 개수
    n1 = (n-2) * (n-2) + 4 * (n-1) * (n-2)
    n2 = 4 * (n-2) + 4 * (n-1)
    n3 = 4
    for x, y in zip(dice_list, [n1, n2, n3]):
        answer += x*y
print(answer)