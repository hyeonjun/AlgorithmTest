import math
input = __import__('sys').stdin.readline
n, atk = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
answer = 0
left, right = 1, int(1e18)
while left <= right:
    mid = (left + right) // 2 # 체력
    # mid = left + (right - left) // 2
    # mid = (left + right) >> 1
    hp, attack = mid, atk
    for t, a, h in room:
        if t == 1: # 몬스터
            hp -= (math.ceil(h / attack) - 1) * a # 몬스터 공격 횟수 * 몬스터 공격력
            if hp <= 0: break
        else: # 포션
            attack += a
            hp = min(hp+h, mid)

    if 0 < hp:
        right = mid -1
        answer = mid
    else:
        left = mid + 1
print(answer)

# ===========================================================

import sys, math
n, atk = map(int, sys.stdin.readline().split())
answer, hp, attack = 0, 0, 0
for i in range(n):
    t, a, h = map(int, sys.stdin.readline().split())
    if t == 1: # 몬스터
        attack = -(a * (math.ceil(h / atk) - 1))
    else: # 포션
        atk += a
        attack = h
    hp += attack
    if hp > 0:
        hp = 0 # 최대 생명력일 때 포션 먹을 때
    answer = max(answer, abs(hp))
print(answer+1)