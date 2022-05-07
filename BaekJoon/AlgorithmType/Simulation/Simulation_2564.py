x, y = map(int, input().split())
arr = []
n = int(input())

def calc(dir, dis): # 한 줄로 있다고 생각하고 넣음
    if dir == 1: # 북쪽
        return y+dis
    elif dir == 2: # 남쪽
        return -dis
    elif dir == 3: # 서쪽
        return y-dis
    else:
        return -x-y+dis

for _ in range(n):
    dirs, distance = map(int, input().split())
    arr.append(calc(dirs, distance))

dong = calc(*list(map(int, input().split())))

answer = 0
for d in arr:
    value = abs(dong - d)
    if x + y > value:
        answer += value
    else:
        answer += 2 * (x+y) - value
print(answer)