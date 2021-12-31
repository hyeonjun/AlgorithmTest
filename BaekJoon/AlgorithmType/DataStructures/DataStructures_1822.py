a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
answer = sorted(A-B)
print(len(answer))
if len(answer):
    print(*answer)