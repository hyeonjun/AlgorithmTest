k, l = map(int, input().split())
sugang = {}
for i in range(l):
    num = input()
    sugang[num] = i
cnt = 0
for i in sorted(sugang.items(), key=lambda x:x[1]):
    if cnt == k:
        break
    print(i[0])
    cnt += 1