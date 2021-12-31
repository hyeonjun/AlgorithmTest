n = int(input())
num = list(map(int, input().split()))
stack = []
target = 1
while num:
    if target == num[0]:
        num.pop(0)
        target += 1
    else:
        stack.append(num.pop(0))
    while stack and stack[-1] == target:
        stack.pop()
        target += 1
print('Nice' if not stack else 'Sad')