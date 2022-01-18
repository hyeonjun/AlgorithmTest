A, a, B, b, P = map(int, input().split())
# A와 B 둘다 개별적으로 P에 들어가는 경우
# B 안에 A가 들어가는 경우
# A 안에 B가 들어가는 경우
if (A+B <= P) or (A <= b and B <= P) or (B <= a and A <= P):
    print('Yes')
else:
    print('No')