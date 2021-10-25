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

"""
점 세개가 한 직선상에 있을 수 있고, 네 개의 점이 한 직선상에 있을 수 있다.
그래서 ccw(A,B,C) * ccw(A,B,D) < 0, ccw(C,D,A) * ccw(C,D,B) < 0을
ccw(A,B,C) * ccw(A,B,D) <= 0, ccw(C,D,A) * ccw(C,D,B) <= 0로 바꿔주면 된다.
하지만 ABCD가 한 직선상에 위 조건을 만족하지만 이는 교차하지 않는다.
한 집단의 max값이 다른 집단의 min값보다 크다는 조건을 만족하면 된다.
"""
answer = 0
if ccw(x1, y1, x2, y2, x3 ,y3) * ccw(x1, y1, x2, y2, x4, y4) == 0 and \
        ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) == 0:
    if min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and \
            min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4):
        answer = 1
elif ccw(x1, y1, x2, y2, x3 ,y3) * ccw(x1, y1, x2, y2, x4, y4) <= 0 and \
        ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2) <= 0:
    answer = 1
print(answer)