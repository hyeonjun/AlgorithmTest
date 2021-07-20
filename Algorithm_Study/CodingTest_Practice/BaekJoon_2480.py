"""
같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
"""
def solution(dice):
    if dice[0] == dice[1] == dice[2]:
        return 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[1] == dice[2]:
        return 1000 + dice[1] * 100
    elif dice[0] == dice[2]:
        return 1000 + dice[0] * 100
    else:
        return max(dice) * 100

print(solution([3,6,3])) # 1300
print(solution([2,2,2])) # 12000
print(solution([6,2,5])) # 600

def solution(dice):
    dice.sort()
    if len(set(dice)) == 1:
        return 10000 + dice[0] * 1000
    elif len(set(dice)) == 2:
        return 1000 + dice[1] * 100
    else:
        return max(dice) * 100

print(solution([3,6,3])) # 1300
print(solution([2,2,2])) # 12000
print(solution([6,2,5])) # 600