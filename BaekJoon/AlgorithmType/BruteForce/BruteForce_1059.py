l = int(input())
s = [0]+sorted(map(int, input().split()))
n = int(input())

if n in s:
    print(0)
else:
    left, right = 0, 0
    for i in s:
        if n > i:
            left = i+1 # 가능한 첫 숫자
        else:
            right = i-1 # 가능한 끝 숫자
            break
    #                n 미만의 가능한 숫자 n 초과의 가능한 숫자
    print(right - left + (right - n) * (n - left))