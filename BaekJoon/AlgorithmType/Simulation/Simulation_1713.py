n = int(input())
v = int(input())
students = list(map(int, input().split()))
picture = [] # 사진틀
score = [] # 사진틀 인덱스와 추천 수

for i in students:
    if i in picture:
        idx = picture.index(i)
        score[idx] += 1
    else:
        if len(picture) >= n:
            idx = score.index(min(score))
            del picture[idx]; del score[idx]
        picture.append(i)
        score.append(1)
picture.sort()
print(*picture)