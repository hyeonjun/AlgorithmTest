k = int(input())-1
n = int(input())
time = 0
while True:
    t, z = input().split()
    time += int(t)
    if time >= 210:
        print(k+1)
        break
    if z == 'T':
        k = (k+1) % 8