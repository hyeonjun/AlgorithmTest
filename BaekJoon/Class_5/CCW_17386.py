"""
(x1, y1), (x2, y2)를 지나는 직선의 방정식
=> y-y1 = (y2-y1) / (x2-x1) * (x-x1)
=> x -> x3, y -> y3로 바꿔 정리하면
=> (x2 - x1) * (y3 - y1)

한 직선에서 다른 직선의 각 점으로 향하는 방향이 시계, 반시께로 구분되어지면
이 두 직선은 교차한다.

(x1, y1) : A
(x2, y2) : B -> A - B 직선
(x3, y3) : C
(x4, y4) : D -> C - D 직선

1. ccw(A,B,C) * ccw(A,B,C) < 0 : 교차한다
2. ccw(C,D,A) * ccw(C,D,B) < 0 : 교차한다
1과 2 모두 만족하면 교차하는 것으로 판단
"""
import sys
input = sys.stdin.readline
x1, y1, x2 ,y2 = map(int, input().split())
x3, y3, x4 ,y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

if ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4) < 0 and \
        ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) < 0:
    print(1)
else:
    print(0)