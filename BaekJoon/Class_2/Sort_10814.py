n = int(input())
member = [list(input().split()) for _ in range(n)]
member.sort(key=lambda x:int(x[0]))
for i in member:
    print(int(i[0]), i[1])