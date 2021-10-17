# 매우매우 어렵다..!
from itertools import combinations
n, s = map(int, input().split())
seq = list(map(int, input().split()))
left, right = seq[:n//2], seq[n//2:]

l_sum, r_sum = [], []
for i in range(len(left)+1):
    for c in combinations(left, i):
        l_sum.append(sum(c))
for i in range(len(right)+1):
    for c in combinations(right, i):
        r_sum.append(sum(c))
l_sum.sort()
r_sum.sort()

# l_sum -> start가 움직이고, r_sum -> end가 움직임
# 각 l과 r에서의 부분수열의 합을 구함.
lidx, ridx = 0, len(r_sum)-1
answer = 0 # s가 되는 경우의 수
while lidx < len(l_sum) and ridx >= 0:
    tmp = l_sum[lidx] + r_sum[ridx]
    if tmp == s:
        lidx += 1
        ridx -= 1
        # a가 있는 r_sum 리스트에 a와 같은 값이 x개 있고
        # b가 있는 l_sum 리스트에 b와 같은 값이 y개 있다면
        # 경우의 수가 총 x * y개가 된다
        lsame, rsame = 1, 1
        while lidx < len(l_sum) and l_sum[lidx] == l_sum[lidx-1]:
            lsame += 1
            lidx += 1
        while ridx >= 0 and r_sum[ridx] == r_sum[ridx+1]:
            rsame += 1
            ridx -= 1
        answer += lsame * rsame
    elif tmp < s:
        if lidx+1 < len(l_sum):
            lidx += 1
        else:
            break
    else:
        if ridx-1 >= 0:
            ridx -= 1
        else:
            break
print(answer-1 if s == 0 else answer)