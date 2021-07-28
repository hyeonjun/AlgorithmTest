# -*- coding:utf-8 -*-
def solution(k, room_number): # 효율성 실패
    answer = []
    room = [False for _ in range(k + 1)]

    for i in room_number:
        if not room[i]:
            answer.append(i)
            room[i] = True
        else:
            for j in range(i + 1, k + 1):
                if not room[j]:
                    answer.append(j)
                    room[j] = True
                    break
    return answer

print(solution(10, [1,3,4,1,3,1])) # [1,3,4,2,5,6]


def solution(k, room_number):
    import sys
    sys.setrecursionlimit(100000)

    answer = []
    dic = dict() # 배정한 번호 : 해당 방 번호를 원하는 자에게 배정할 다음 번호

    def findRoom(num):
        if num not in dic:
            dic[num] = num + 1
            return num

        empty = findRoom(dic[num])
        dic[num] = empty + 1
        return empty

    for i in room_number:
        num = findRoom(i)
        answer.append(num)

    return answer

print(solution(10, [1,3,4,1,3,1])) # [1,3,4,2,5,6]