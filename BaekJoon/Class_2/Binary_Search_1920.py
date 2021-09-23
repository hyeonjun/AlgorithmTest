N = int(input())
A = sorted(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

def BinarySearch(b, start, end):
    while start <= end:
        mid = (start+end) // 2
        if b == A[mid]:
            return 1
        if A[mid] <= b:
            start = mid+1
        else:
            end = mid-1
    return 0
for b in B:
    print(BinarySearch(b, 0, N-1))
