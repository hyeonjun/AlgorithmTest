card = {}
for _ in range(int(input())):
    n = int(input())
    if n not in card:
        card[n] = 1
    else:
        card[n] += 1
card = sorted(card.items(), key=lambda x: (-x[1], x[0]))
print(card[0][0])