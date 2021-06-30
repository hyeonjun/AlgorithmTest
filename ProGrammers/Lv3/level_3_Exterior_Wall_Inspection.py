# -*- coding:utf-8 -*-
def solution(n, weak, dist):
    from itertools import permutations
    weak_len = len(weak)
    for i in range(weak_len):  # 시계-반시계 방향 문제는 배열을 두배로 늘린다
        weak.append(weak[i] + n)  # 두 배로 늘리면 방향 고민할 필요가 없어진다

    answer = len(dist) + 1  # 투입가능 친구수 +1
    candidates = list(map(list, permutations(dist, len(dist))))  # 투입할 친구 순서

    for i in range(weak_len):
        start = [weak[j] for j in range(i, i + weak_len)]

        for can in candidates:
            idx, cnt = 0, 1  # 거리, 친구 수
            check_len = start[0] + can[0]  # 친구가 확인할 수 있는 최대 거리

            for f in range(weak_len):
                if start[f] > check_len: # 확인 가능한 거리보다 확인해야할 거리가 더 크면
                    cnt += 1 # 친구 투입
                    if cnt > len(can): # 더이상 투입할 인원이 없을 경우
                        break
                    idx += 1 # 다음 친구의 거리 구하기
                    check_len = start[f] + can[idx] # 출발 할 시점 + 이동 가능 거리
            answer = min(answer, cnt)

    if answer > len(dist): # 모두 체크 불가능
        return -1

    return answer

print(solution(12, [1,5,6,10], [1,2,3,4])) # 2
print(solution(12, [1,3,4,9,10], [3,5,7])) # 1