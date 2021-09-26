n, m = map(int, input().split())
card = list(map(int, input().split()))
result = []
from itertools import permutations
for i in permutations(card, 3):
    data = sum(i)
    if data <= m:
        result.append(data)
print(sorted(result)[-1])