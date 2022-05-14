from collections import Counter
n, m = map(int, input().split())
print(Counter(list(map(int, input().split()))).most_common(1)[0][1])
