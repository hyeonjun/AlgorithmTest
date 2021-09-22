# 2920
scale = list(map(int, input().split()))
sort_scale = sorted(scale)
if sort_scale == scale:
    print("ascending")
elif sort_scale[::-1] == scale:
    print("descending")
else:
    print("mixed")
    
# 3052
remainder = set()
for _ in range(10):
    remainder.add(int(input()) % 42)
print(len(remainder))

# 8958
for _ in range(int(input())):
    result = input()
    score = []
    for r in result:
        score.append(0) if r == 'X' else score.append(score[-1]+1) if len(score) > 0 else score.append(1)
    print(sum(score))
