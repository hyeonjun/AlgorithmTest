# 2475
print(sum([i**2 for i in map(int, input().split())]) % 10)

# 2562
score = []
for _ in range(9):
    score.append(int(input()))
max_s = max(score)
for i, v in enumerate(score):
    if max_s == v:
        print('{0}\n{1}'.format(v, i+1))

# 2577
number = 1
for _ in range(3):
    number *= int(input())
number = str(number)
for i in range(10):
    print(number.count(str(i)))