# Binary Search
_ = int(input())
N = sorted(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

def binary(n, N, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if n == N[mid]:
        return N[start:end+1].count(n)
    elif n < N[mid]:
        return binary(n, N, start, mid-1)
    else:
        return binary(n, N, mid+1, end)

dic = {}
for n in N:
    start = 0
    end = len(N)-1
    if n not in dic:
        dic[n] = binary(n, N, start, end)

print(' '.join(str(dic[m]) if m in dic else '0' for m in M))

# Hash
_ = int(input())
N = sorted(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

dic = {}
for n in N:
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1
print(' '.join(str(dic[m]) if m in dic else '0' for m in M))