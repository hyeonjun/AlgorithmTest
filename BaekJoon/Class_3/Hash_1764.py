n, m = map(int, input().split())
non_listen = set(input() for _ in range(n))
non_see = set(input() for _ in range(m))
reulst = non_see & non_listen # set으로 교집합구하기
print(len(reulst))
for i in sorted(reulst):
    print(i)