from itertools import permutations
num = [i for i in permutations(range(1, 10), 3)]
for _ in range(int(input())):
    test, strike, ball = map(int, input().split())
    test = list(map(int, str(test)))
    remove = 0
    for i in range(len(num)):
        s, b = 0, 0
        i -= remove
        for x, y in zip(num[i], test):
            if x == y:
                s +=1
            elif x in test:
                b += 1
        if s != strike or b != ball:
            num.remove(num[i])
            remove += 1
print(len(num))