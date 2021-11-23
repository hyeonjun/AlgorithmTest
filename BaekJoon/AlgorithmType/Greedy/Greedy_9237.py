"""
4
4 3
3 3 3
2 2 3 2
1 1 2 2
0 0 1 1
0 0 0 0
"""
n = int(input())
t = sorted(map(int, input().split()), reverse=True)
for i in range(n):
    t[i] += i+1
print(max(t)+1)



