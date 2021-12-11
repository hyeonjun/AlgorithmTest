card = [i for i in range(1, 21)]
for _ in range(10):
    s, e = map(int, input().split())
    card[s-1:e] = list(reversed(card[s-1:e]))
print(*card)