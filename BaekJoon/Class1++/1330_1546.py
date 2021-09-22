# 1330
a, b = map(int, input().split())
print('>') if a > b else print('<') if a < b else print('==')

# 1546
n = int(input())
score = list(map(int, input().split()))
max_s = max(score)
new_score = [(s/max_s)*100 for s in score]
print(sum(new_score)/n)