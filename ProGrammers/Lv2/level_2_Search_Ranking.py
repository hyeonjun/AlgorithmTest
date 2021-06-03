from collections import defaultdict
from itertools import combinations
def solution(info, query):
    answer = []

    # 1. 지원자 정보 parsing
    infomation = defaultdict(list)
    for i in info:
        i = i.split()
        key, score = i[0:4], int(i[4])

        # 1-1. 점수를 제외한 4가지 조건으로 16가지 경우의 수 만듬
        for j in range(5):
            for c in combinations(key, j):
                k=''.join(c)
                infomation[k].append(score)

    # 2. infomation의 key에 따른 점수 정렬
    for key in infomation.keys():
        infomation[key].sort()

    # 3. 조건 parsing
    for i in query:
        i = i.split(' ')
        # 3-1. 'and'와 '-' 제외하기 -> 필요조건으로만 key 생성
        q = list(filter(lambda x: x != 'and' and x != '-', i))

        key = ''.join(q[:-1])
        score = int(q[-1])

        # 3-2. 이분탐색으로 조건에 맞는 지원자 수 구함
        count = 0
        if key in infomation.keys():
            value = infomation[key]
            start, end = 0, len(value)
            while start <= end and start < len(value):
                mid = (start+end) //2
                if value[mid] < score:
                    start = mid+1
                else:
                    end = mid -1
            count = len(value) - start
        answer.append(count)
    return answer



info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

def solution(info, query): # 정확성만 통과
    answer = [0] * len(query)

    def isCheck(q, m):
        for k in range(4):
            if m[k] != q[k] and q[k] != '-':
                return False
        return True

    for i in range(len(query)):
        q = query[i].split(' ')
        q = list(filter(lambda x: x != 'and', q))
        for j in info:
            m = j.split(' ')
            if isCheck(q, m) and int(m[4]) >= int(q[4]):
                answer[i] += 1
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# print(solution(info, query))