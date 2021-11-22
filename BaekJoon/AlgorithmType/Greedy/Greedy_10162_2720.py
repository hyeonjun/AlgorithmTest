# 10162
t = int(input())
if t % 10 != 0:
    print(-1)
else:
    answer = 0
    btn = [t // 300, (t%300) // 60, ((t%300) % 60) // 10]
    print(*btn)

# 2720
for _ in range(int(input())):
    money = int(input())
    q, d, n, p = 25, 10, 5, 1
    print(money//q, (money%q)//d, ((money%q)%d)//n, (((money%q)%d)%n)//p)