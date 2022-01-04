A = input()
B = input()
a = [0 for _ in range(26)]
b = [0 for _ in range(26)]
for i in A:
    a[ord(i) - ord('a')] += 1
for i in B:
    b[ord(i) - ord('a')] += 1
answer = 0
for x, y in zip(a, b):
    answer += abs(x-y)
print(answer)