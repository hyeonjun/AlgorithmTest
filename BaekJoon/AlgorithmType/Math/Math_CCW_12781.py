"""
CCW (Counterclockwise)
외적을 이용하여 유도할 수 있음 -> CCW 알고리즘을 이용하여 세점의 방향성을 알 수 있음
각각의 점 A(x1, y1), B(x2, y2), C(x3, y3) 이라고 좌표를 두고, A,B,C 순서로 방향관꼐를 구한다면,
CCW 함수의 return 값은  x1y2 + x2y3 + x3y1 - (x2y1 + x3y2 + x1y3)이 된다.
return 값이 음수이면 시계방향
양수이면 반시계방향
0이면 세점이 평행하다

이를 통해 선분 교차 판별 문제를 풀어낼 수 있음

선분 CD를 기준으로 점 A와 B의 CCW 값의 부호가 각각 다를 때 선분이 교차한다고 말할 수 있다.
  => CCW(A,B,C) * CCW(A,B,D) <= 0
하지만 <= 라고 해서 무조건 교차하는 것은 아니다.
CCW(C,D,A) * (C,D,B) <= 0 이면서 CCW(A,B,C) * CCW(A,B,D) <= 0 이어야 선분이 교차한다고 말할 수 있다.

하나 더 주의해야할 점은
CCW(C,D,A)*CCW(C,D,B)==0 AND CCW(A,B,C)*CCW(A,B,D)==0 일 때로,
이의 경우 두 AB 선분과 CD 선분이 같은 방향으로 떨어져있을 수도 있고, 겹쳐 있는 부분이 있을 수도 있다.
이 때는 A,B와 C,D의 상대적 위치를 비교해야한다.
A,B 둘 중 좌표가 큰값과 C,D 둘 중 좌표가 큰값을 서로의 작은 값보다 클때만 선분이 교차한다.
"""
def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2-x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if tmp > 0: return 1
    elif tmp < 0: return -1
    else: return 0

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
res1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
res2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
if res1 == -1 and res2 == -1:
    print(1)
else:
    print(0)
