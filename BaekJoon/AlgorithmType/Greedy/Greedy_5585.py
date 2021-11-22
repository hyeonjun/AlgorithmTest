money = 1000 - int(input())
arr = [500, 100, 50, 10, 5, 1]
answer = 0
for i in arr:
    answer += money//i
    money %= i
print(answer)