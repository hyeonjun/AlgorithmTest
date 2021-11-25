n = int(input())
rope = [int(input()) for _ in range(n)]
rope.sort(reverse=True)
for i in range(n):
    rope[i] = rope[i] * (i+1)
print(max(rope))