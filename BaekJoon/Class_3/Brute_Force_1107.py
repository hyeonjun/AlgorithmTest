n = int(input())
m = int(input())
button = set(i for i in range(0,10))
if m > 0:
    button -= set(map(int, input().split()))
current = 100
result = abs(current - n)

def check(ch):
    for i in str(ch):
        if int(i)not in button:
            return False
    return True
# 희망 채널은 500000 이하지만, +와 -가 있기때문에 100만 채널까지 확인하는 것이 맞음.
for ch in range(1000000): # 희망채널이 400000, 고장버튼 [1,2,3,4,5]일 경우 600000에서 내려가는게 더 빠름
    if not check(ch):
        continue
    result = min(result, abs(n - ch)+len(str(ch)))
print(result)