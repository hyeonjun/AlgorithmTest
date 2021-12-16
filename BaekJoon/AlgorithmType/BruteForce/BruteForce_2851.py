mushroom = [int(input()) for _ in range(10)]
answer = 0
for i in mushroom:
    answer += i
    if answer >= 100:
        if answer - 100 > 100 - (answer-i):
            answer -= i
        break
print(answer)