# 팩토리얼의 0 개수는 5가 곱해진 개수로 구할 수 있음
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    x = int(input())
    answer = 0
    i = 5
    while i <= x:
        answer += x // i
        i *= 5
    print(answer)