n = int(input())
A = list(map(int, list(input())))
B = list(map(int, list(input())))

def change(num):
    return 1 if num == 0 else 0

def switch(lst, count):
    if count == 1:
        lst[0] = change(lst[0])
        lst[1] = change(lst[1])
    for i in range(1, n):
        if lst[i-1] != B[i-1]:
            count += 1
            lst[i-1] = change(lst[i-1])
            lst[i] = change(lst[i])
            if i != n-1:
                lst[i+1] = change(lst[i+1])
    return count if lst == B else -1

result1 = switch(A[:], 0) # 첫 번째 안바꿈
result2 = switch(A[:], 1) # 첫 번째 바꿈
if result1 >= 0 and result2 >= 0:
    print(min(result1, result2))
elif result1 >= 0 and result2 < 0:
    print(result1)
elif result1 < 0 and result2 >= 0:
    print(result2)
else:
    print(-1)