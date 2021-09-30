string = list(input().split('-')) # -를 기준으로 괄호로 묶으면 최소값을 얻을 수 있다.
num = []
for i in string:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    num.append(cnt)
result = num[0]
for i in range(1, len(num)):
    result -= num[i]
print(result)