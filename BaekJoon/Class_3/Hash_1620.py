import sys
n, m = map(int, input().split())
dictionay_num = dict()
dictionay_name = dict()
for i in range(1, n+1):
    name = sys.stdin.readline().strip()
    dictionay_name[name] = i
    dictionay_num[i] = name

for _ in range(m):
    problem = sys.stdin.readline().strip()
    try:
        print(dictionay_name[problem])
    except:
        print(dictionay_num[int(problem)])