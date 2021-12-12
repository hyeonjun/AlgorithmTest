n = int(input())
switch = [''] + list(map(int, input().split()))

def change(idx):
    return (switch[idx] + 1) % 2

for _ in range(int(input())):
    a, idx = map(int, input().split())
    if a == 1: # 남자
        for i in range(idx, n+1, idx):
            switch[i] = change(i)
    else: # 여자
        switch[idx] = change(idx)
        for i in range(n//2):
            if idx + i > n or idx - i < 1:
                break
            if switch[idx+i] == switch[idx-i]:
                switch[idx+i] = change(idx+i)
                switch[idx-i] = change(idx-i)
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=" ")
    if i % 20 == 0:
        print()