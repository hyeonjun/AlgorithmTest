"""
f(1) = f(2) = f(3) = 1
n > 3:
 f(n) = f(n-2) + f(n-3)
"""

for _ in range(int(input())):
    n = int(input())
    seq = [1, 1, 1]
    for i in range(4, n+1):
        seq.append(seq[i-4] + seq[i-3])
    print(seq[n-1])