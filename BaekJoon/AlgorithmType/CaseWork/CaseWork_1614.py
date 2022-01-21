"""
횟수 : 0  1  2   3
엄지 : 0, 8, 16, 24  .. => 8
검지 : 1, 7, 9,  15, 17, 23 => 6 <-> 2 증가
중지 : 2, 6, 10, 14, 18 => 4
약지 : 3  5  11  13  19 => 2 <-> 6 증가
새끼 : 4  12 20  28  .. => 8

위치, 횟수
위치 = 1 => 8 * 횟수
위치 = 5 => 8 * 횟수 + 4
나머지 => 4 * 횟수 + 1 + (m이 홀수면 4-위치, m이 짝수면 위치-2)
"""
idx = int(input())
cnt = int(input())
if idx == 1:
    answer = 8 * cnt
elif idx == 5:
    answer = 8 * cnt + 4
else:
    answer = 4 * cnt + 1 + (4-idx if cnt % 2 else idx-2)
print(answer)