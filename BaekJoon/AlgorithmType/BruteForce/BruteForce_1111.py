"""
y = ax + b 일 때,
y1 = a * x1 + b / y2 = a * x2 + b
 => a = (y2-y1) / (x2-x1)
    b = y1 - a * x1
"""
n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print('A')
elif n == 2:
    if arr[0] != arr[1]:
        print('A')
    else:
        print(arr[1])
else: # 길이 3 이상이면 기울기와 절편을 구해 패턴이 맞는지 확인
    if arr[0] - arr[1] == 0:
        a = 0
    else:
        a = (arr[2] - arr[1]) // (arr[1] - arr[0])
    b = arr[1] - arr[0] * a
    answer = None
    for i in range(n-1):
        nxt = arr[i] * a + b
        if arr[i+1] != nxt:
            answer = 'B'
    print(arr[-1] * a + b if answer is None else answer)