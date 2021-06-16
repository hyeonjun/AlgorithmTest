# -*- coding:cp949 -*-
def solution(n):
    answer = []
    def move(n, start, to, via):
        if n == 1:
            answer.append([start, to])
            return
        move(n - 1, start, via, to)  # A���� C�� ���ļ� B��
        answer.append([start, to])  # ������ ������ A���� C��
        move(n - 1, via, to, start)  # B���� A�� ���ļ� C��
    move(n, 1, 3, 2)
    return answer

print(solution(3))

def solution(n):
    def move(n, start, to, via):
        if n == 1: return [[start, to]]
        return move(n-1, start, via, to) + [[start, to]] + move(n-1, via, to, start)
    return move(n, 1, 3, 2)

print(solution(3))
