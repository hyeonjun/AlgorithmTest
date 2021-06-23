# 거스름돈
def solution(price):
    changes = [500, 100, 50, 10, 5, 1]
    C = 1000 - price
    count = 0
    for i in changes:
        count += C // i
        C %= i
    return count

print(solution(380))
# =============================================================================

# 뒤집기
def solution(string):
    count_0 = 0 # 전부 0
    count_1 = 0 # 전부 1
    if string[0] == "1":
        count_0 += 1
    else:
        count_1 += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == '1':
                count_0 += 1
            else:
                count_1 += 1
    return min(count_0, count_1)

print(solution("0001100")) # 1
# =============================================================================

# 등수 매기기
def solution(n, rank):
    rank.sort() # 오름 차순 정렬
    answer = 0
    for i in range(n):
        answer += abs((i+1) - rank[i])
    return answer

print(solution(5, [1,5,3,1,2]))
# =============================================================================

# 배
def solution(n, crane, m, box):
    if max(crane) < max(box):
        return -1

    answer = 0
    box.sort(reverse=True)
    crane.sort(reverse=True)

    while box:
        answer += 1
        for c in range(n):
            for b in range(len(box)):
                if crane[c] >= box[b]:
                    box.pop(b)
                    break
    return answer

# n = int(input())
# crane = list(map(int, input().split()))
# m = int(input())
# box = list(map(int, input().split()))
# print(solution(n, crane, m, box))

print(solution(3, [6,8,9], 5, [2,5,2,4,9]))

def solution(n, crane, m, box):
    if max(crane) < max(box):
        return -1

    # 각 크레인이 현재 옮겨야할 박스의 번호
    positions = [0] * n

    # 각 박스를 옮겼는지의 여부
    checked = [False] * m

    crane.sort(reverse=True)
    box.sort(reverse=True)

    result = 0
    count = 0

    while True:
        if count == len(box): # 박스 모두 옮겼으면 종료
            break
        for i in range(n): # 모든 크레인에 대해 각각 처리
            while positions[i] < len(box):
                if not checked[positions[i]] and crane[i] >= box[positions[i]]:
                    checked[positions[i]] = True
                    positions[i] += 1
                    count += 1
                    break
                positions[i] += 1
        result += 1
    return result

print(solution(3, [6,8,9], 5, [2,5,2,4,9]))


